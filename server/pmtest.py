from getMongoDB import get_database
#print(get_database())
hackysu = get_database()
testCollection = hackysu['test_items']
testItem = {
    "_id": "thefirst",
    "testTestTest" : 2024,
    }
testCollection.insert_one(testItem)