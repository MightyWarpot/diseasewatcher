import json
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(
    "mongodb+srv://user:iBMu1UIQhIzoW8Qn@cluster0.uq4ht.mongodb.net/outbreak_articles?retryWrites=true&w=majority")
db = client.outbreak_articles
col = db.outbreak_details

test = col.find_one({'location': 'China'})

print(test)
# print(client.list_database_names())
# Issue the serverStatus command and print the results
serverStatusResult = db.command("serverStatus")
# pprint(serverStatusResult)





# with open('data.json') as f:
#     entries = json.load(f)

# print(entries[0]['location'])





def location(location_str):


    with open('data.json') as f:
        entries = json.load(f)
