
import sys
import pprint

from configs import BITHUMB_CONNECT, BITHUMB_SECRET
from api.bithumb import BithumbAPI

if __name__ == "__main__":
    api_key = BITHUMB_CONNECT
    api_secret = BITHUMB_SECRET

    api = BithumbAPI(api_key, api_secret);

    #
    # public api
    #
    # /public/ticker
    # /public/recent_ticker
    # /public/orderbook
    # /public/recent_transactions

    result = api.xcoinApiCall("/public/ticker", {
    "order_currency" : "BTC",
    "payment_currency" : "KRW"
    });
    print("status: " + result["status"]);
    print("last: " + result["data"]["closing_price"]);


