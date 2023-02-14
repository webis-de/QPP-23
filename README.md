# A Large-Scale Dataset for Known-Item Question Performance Prediction

Please find the dataset at [https://files.webis.de/corpora/corpora-webis/known-item-question-performance-prediction/](https://files.webis.de/corpora/corpora-webis/known-item-question-performance-prediction/).

Authors: Maik Fröbe, Eric Oliver Schmidt and Matthias Hagen

## Abstract
Searchers who can't satisfy their known-item information need using a search engine might ask their information need on question-answering platforms, hoping that the active discussion with other users solves the known-item question. Given that much effort can go into those discussions, effective query performance prediction might guide searchers in formulating good questions or not posting hopeless questions. To foster future research on novel applications of query performance prediction, especially in the light of the upcoming tip-of-the-tongue known-item retrieval track at TREC, we build a large-scale dataset for known-item question performance prediction containing 1.3 million known-item questions, of which 47 % are marked as solved. We use the time it took to solve a question (or the absence of a solution) as the performance of the question to evaluate the effectiveness of 7 standard pre-retrieval query performance predictors: all of them cannot predict the performance of known-item questions.

## Analyze TOMT subreddit

## Description of code structure
`extract-solved-comment-test.ipynb` contains our code for extracting Gold Answers from the TOMT subreddit dataset. It loads in the TOMT subreddit dataset and extends it with the `solved_utc`, `chosen_answer` and `links_on_answer_path` attributes.
In addition, we rename the Reddit attributes `selftext` to `content` and `title`to `subject`, as it is common in other Q&A datasets, such as Yahoo!-Answers.
We iterate through all questions and call the `find_gold_answer(qa)` method which traverses the comment tree of each question. It expects a Pandas dataframe row with all the required attributes (i.e. `author`, `created_utc`, `link_flair_text`, `num_comments`, `comments`).
This will extract all the links on the comments path to the Gold Answer are extracted and determine the `solved_dates` that correspond to the `created_utc` of the Gold Answer.
There is a possibility to customize the Gold Answer heuristic, which is based on the presence of the keywords "yes", "thank", "solved", "amazing" is this choice seemed to work adequately in pilot experiments and precision and recall experiments (see [below](## Precision and Recall experiments)). Another possible adaptation is to also consider questions without a value of `link_flair_text`, i.e. questions that could be solved but are not officially marked as `Solved`.

## Precision and Recall experiments
