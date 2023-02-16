# A Large-Scale Dataset for Known-Item Question Performance Prediction

The paper associated to this repository and dataset is currently under review.
This repository contains all the code to re-run and reproduce the crawling and experiments.

You can find the ready-to-use dataset at [https://files.webis.de/corpora/corpora-webis/known-item-question-performance-prediction/](https://files.webis.de/corpora/corpora-webis/known-item-question-performance-prediction/).

# Structure of this repository

## Analyze TOMT subreddit
### Analyze categories

### Analyze solved questions
`analyze-tomt-solved.ipynb` contains the code to analyze the categories of the solved questions and the waiting time. It also contains samples for precision and recall experiments.

## Description of code structure
`extract-solved-comment-test.ipynb` contains our code for extracting Gold Answers from the TOMT subreddit dataset. It loads in the TOMT subreddit dataset and extends it with the `solved_utc`, `chosen_answer` and `links_on_answer_path` attributes.
In addition, we rename the Reddit attributes `selftext` to `content` and `title`to `subject`, as it is common in other Q&A datasets, such as Yahoo!-Answers.
We iterate through all questions and call the `find_gold_answer(qa)` method which traverses the comment tree of each question. It expects a Pandas dataframe row with all the required attributes (i.e. `author`, `created_utc`, `link_flair_text`, `num_comments`, `comments`).
This will extract all the links on the comments path to the Gold Answer are extracted and determine the `solved_dates` that correspond to the `created_utc` of the Gold Answer.
There is a possibility to customize the Gold Answer heuristic, which is based on the presence of the keywords "yes", "thank", "solved", "amazing" is this choice seemed to work adequately in pilot experiments and precision and recall experiments (see [below](#precision-and-recall-experiments)). Another possible adaptation is to also consider questions without a value of `link_flair_text`, i.e. questions that could be solved but are not officially marked as `Solved`.

## Precision and Recall experiments
We measure the precision and recall of our approach by annotating 50 random questions from the corpus and 50 questions for which our heuristic extracts a solved answer (those questions were not used to develop the rules), finding that our approach has a precision of 92 % and a recall of 78 %. `analyze-tomt-solved.ipynb` contains the code that extracts these random questions. These samples can also be found in `sample-data` as `csv` files.

## Sample data
We provide sample data extracted in `analyze-tomt-solved.ipynb`. The `sample-data` folder contains sample questions from the TOMT subreddit that were solved within a day, a week, a month, a year or later. There are also two random datasets for recall and precision experiments.
