from configs import BITHUMB_CONNECT, BITHUMB_SECRET
from api.bithumb import BithumbAPI
from db import VCoinDB

def insertTicker(api, db, order_currency, payment_currency):
    status, data = api.getTicker(order_currency, payment_currency)
    if status == "0000":
        db.insertTicker({**data, "order_currency":order_currency, "payment_currency":payment_currency})

def insertOrderbook(api, db, order_currency, payment_currency):
    status, data = api.getOrderbook(order_currency, payment_currency)
    if status == "0000":
        db.insertOrderbook(data)



if __name__ == "__main__":
    api = BithumbAPI(BITHUMB_CONNECT, BITHUMB_SECRET)
    db = VCoinDB("localhost", 27017)

    insertTicker(api, db, 'BTC', 'KRW')
    insertOrderbook(api, db, 'BTC', 'KRW')

    db.dump()


