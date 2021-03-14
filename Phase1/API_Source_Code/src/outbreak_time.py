import json
import datetime
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

# this function works assuming the date format is always in "Month xx, year" format

# def date(dtime):

def time_filter(dtime, col):
    date_matches = []
    if dtime == '': 
        return date_matches
    else:

        for doc in col.find({"date": dtime}):
            # print(doc['title'].strip())
            # print(doc['location'].strip())
            # print(doc['date'].strip())

            date_match = {
                'title': doc['title'].strip(),
                'date': doc['date'].strip(),
                'location': doc['location'].strip(),
                'region': doc['region'].strip(),
                'url': doc['url'].strip(),
                'disease': doc['disease'].strip(),
                'body': doc['body']
            }

            date_match_copy = date_match.copy()

            date_matches.append(date_match_copy)

        return date_matches
