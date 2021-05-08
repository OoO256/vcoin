import pymongo

dbClient = pymongo.MongoClient('localhost', 27017, serverSelectionTimeoutMS = 3000)
db = dbClient["vcoin"]
tickers = db["tickers"]
orderbooks = db["orderbooks"]

for row in tickers.find():
    print(row)

for row in orderbooks.find():
    print(row)
