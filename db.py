import pymongo

class VCoinDB:
    dbClient = None
    db = None
    tickers = None
    orderbooks = None

    def __init__(self, host, port):
        self.dbClient = pymongo.MongoClient(host, port, serverSelectionTimeoutMS=3000)
        self.db = self.dbClient["vcoin"]
        self.tickers = self.db["tickers"]
        self.orderbooks = self.db["orderbooks"]

    def dump(self):
        for row in self.tickers.find():
            print(row)
        for row in self.orderbooks.find():
            print(row)

    def insertTicker(self, data):
        return self.tickers.insert_one(data)

    def insertOrderbook(self, data):
        return self.orderbooks.insert_one(data)