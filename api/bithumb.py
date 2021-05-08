import sys
import time
import math
import base64
import hmac, hashlib
import urllib.parse
import json
import requests

class BithumbAPI:
	api_url = "https://api.bithumb.com"
	api_key = ""
	api_secret = ""

	def __init__(self, api_key, api_secret):
		self.api_key = api_key
		self.api_secret = api_secret

	def body_callback(self, buf):
		self.contents = buf

	def microtime(self, get_as_float = False):
		if get_as_float:
			return time.time()
		else:
			return '%f %d' % math.modf(time.time())

	def usecTime(self) :
		mt = self.microtime(False)
		mt_array = mt.split(" ")[:2]
		return mt_array[1] + mt_array[0][2:5]

	def xcoinApiCall(self, endpoint, rgParams):
		endpoint_item_array = {
			"endpoint" : endpoint
		}

		uri_array = dict(endpoint_item_array, **rgParams)
		str_data = urllib.parse.urlencode(uri_array)
		nonce = self.usecTime()

		data = endpoint + chr(0) + str_data + chr(0) + nonce
		utf8_data = data.encode('utf-8')

		key = self.api_secret
		utf8_key = key.encode('utf-8')

		h = hmac.new(bytes(utf8_key), utf8_data, hashlib.sha512)
		hex_output = h.hexdigest()
		utf8_hex_output = hex_output.encode('utf-8')

		api_sign = base64.b64encode(utf8_hex_output)
		utf8_api_sign = api_sign.decode('utf-8')

		headers = {
			'Api-Key': self.api_key, 'Api-Sign' : utf8_api_sign, 'Api-Nonce' :  nonce
		}
		url = self.api_url + endpoint
		res = requests.post(url,
		headers=headers)

		print(res.json())

		return res.json()
	
	def getTicker(order_currency, payment_currency):
		result = api.xcoinApiCall("/public/ticker", {
			"order_currency" : order_currency,
			"payment_currency" : payment_currency
		});
		return result['status'], result['data']
	
	def getOrderbook(order_currency, payment_currency):
		result = api.xcoinApiCall("/public/orderbook", {
			"order_currency" : order_currency,
			"payment_currency" : payment_currency
		});
		return result['status'], result['data']