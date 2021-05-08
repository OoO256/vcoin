import pymongo

dbClient = pymongo.MongoClient('localhost', 27017, serverSelectionTimeoutMS = 3000)
db = dbClient["vcoin"]
tickers = db["tickers"]
orderbooks = db["orderbooks"]

tickers.drop()
orderbooks.drop()
