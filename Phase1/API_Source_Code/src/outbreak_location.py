import json
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string

# location_matches = []

def location_filter(location_str, col):
    location_matches = []
    if location_str == '':
        return location_matches


    # location_matches = []
    else:
        for doc in col.find({"location": location_str}):
            # print(doc)
            # print(doc['title'].strip())
            # print(doc['location'].strip())
            # print(doc['date'].strip())

            location_match = {
                'title': doc['title'].strip(),
                'date': doc['date'].strip(),
                'location': doc['location'].strip(),
                'region': doc['region'].strip(),
                'url': doc['url'].strip(),
                'disease': doc['disease'].strip()
            }

            location_match_copy = location_match.copy()

            location_matches.append(location_match_copy)

        return location_matches
