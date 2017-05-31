from pprint import pprint

from pymongo import MongoClient
import pandas as pd

from data_formatter import *


def _connect_mongo(host, port, username, password, db):
    """ A util for making a connection to mongo """

    if username and password:
        mongo_uri = 'mongodb://%s:%s@%s:%s/%s' % (username, password, host, port, db)
        conn = MongoClient(mongo_uri)
    else:
        conn = MongoClient(host, port)


    return conn[db]


def read_mongo(db, collection, query={}, host='localhost', port=27017, username=None, password=None, no_id=False):
    """ Read from Mongo and Store into DataFrame """

    # Connect to MongoDB
    db = _connect_mongo(host=host, port=port, username=username, password=password, db=db)

    # Make a query to the specific DB and Collection
    cursor = db[collection].find({ "droidmon" : { '$exists' : 'true' }  },{"droidmon.api" : 'true' ,"class" : 'true'})

    # Expand the cursor and construct the DataFrame
    #df =  pd.DataFrame(list(cursor))

    # Delete the _id
    if no_id:
        del df['_id']

    return cursor


# df_ben = read_mongo(collection='analysis',db='cuckooBenignDB')
# print("malwares_api_shape: {0}".format(df_mal.shape))
# df_mal.head()
# print("malwares_api_shape: {0}".format(df_ben.shape))
# df_mal.head().to_csv('out_csv.csv', sep='@',encoding='utf-8')