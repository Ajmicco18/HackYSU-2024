from getMongoDB import get_database
#print(get_database())
hackysu = get_database()
testCollection = hackysu['bets']
testItem = {
    "gametime" : "04-06-2024-20-30-00",
    "hometeam":"phillies",
    "awayteam":"braves"
    }
#testCollection.insert_one(testItem)
testCollection.delete_one({"hometeam":"phillies"})