from getMongoDB import get_database
hydb = get_database()

coll = hydb['test_items']
items = coll.find()
bets = [x for x in items]
print(type(bets))