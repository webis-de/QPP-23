from qpptk.global_manager import initialize_ciff_index
from qpptk.parse_queries import QueryParserText
from qpptk.pre_retrieval_predictors import LocalManagerPredictorPre 
import json

query_file_input = '/mnt/ceph/storage/data-in-progress/data-research/web-search/false-memories/reddit-tomt/tomt-dataset-26-01-2023/qpp-sample/qpptk-queries'
query_file_predictions = '/mnt/ceph/storage/data-in-progress/data-research/web-search/false-memories/reddit-tomt/tomt-dataset-26-01-2023/qpp-sample/qpptk-queries-predictions.jsonl'
queries = QueryParserText(query_file_input)

ciff_index = initialize_ciff_index('/mnt/ceph/storage/data-in-progress/data-research/web-search/false-memories/reddit-tomt/tomt-dataset-26-01-2023/qpp-sample/ciff-index/robust04-complete-20200306.ciff')

def run_pre_prediction_process(qid):
    process = LocalManagerPredictorPre(index_obj=ciff_index, query_obj=queries, qid=qid)
    max_idf = process.calc_max_idf()
    avg_idf = process.calc_avg_idf()
    scq = process.calc_scq()
    max_scq = process.calc_max_scq()
    avg_scq = process.calc_avg_scq()
    var = process.calc_var()
    avg_var = process.calc_avg_var()
    max_var = process.calc_max_var()
    return {'qid': qid, 'max-idf': max_idf, 'avg-idf': avg_idf, 'scq': scq, 'max-scq': max_scq, 'avg-scq': avg_scq,
            'var': var, 'max-var': max_var, 'avg-var': avg_var}

with open(query_file_input, 'r') as query_inputs, open(query_file_predictions, 'w') as preds:
    for i in query_inputs:
        i = i.split()[0]
        preds.write(json.dumps(run_pre_prediction_process(i)) + '\n')

