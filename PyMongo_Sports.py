from pymongo import MongoClient
import json
import urllib.parse
username = urllib.parse.quote_plus("Zack_Zack")
password = urllib.parse.quote_plus("ChocolateCake")
client = MongoClient(f'mongodb+srv://{username}:{password}@cluster0.glxcrkj.mongodb.net/')


db = client["hackysu"]
collection = db['bets']


#Loading JSON File
with open("MyBookie_sample.json") as input_file, open("DraftKings_sample.json") as input_file2:
    file_data = json.load(input_file)
    file_data2 = json.load(input_file2)

#Clear out Collection before Writing New Data.
x = collection.delete_many({})

if isinstance(file_data, list):
    collection.insert_many(file_data)
else:
    collection.insert_one(file_data)

if isinstance(file_data, list):
    collection.insert_many(file_data2)
else:
    collection.insert_one(file_data2)

input_file.close()
cur = collection.find()
for doc in cur:
    print(doc)