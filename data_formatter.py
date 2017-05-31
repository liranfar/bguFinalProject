import pprint

from bson import json_util
from pandas.io.json import json_normalize
import json


def convert_to_json_list(db_cursor):
    json_list = list(json.loads(json_util.dumps(db_cursor)))
    return json_list

def merge_lists_and_normalize(malwares,benign):
    merged_list = malwares + benign
    df = json_normalize(merged_list)
    pprint.pprint(len(df.columns))
    return df
