from getMongoDB import get_database
hy = get_database()

cn = hy['test_items']

items = cn.find({"testTestTest" : 2024})
for item in items:
    print(item)