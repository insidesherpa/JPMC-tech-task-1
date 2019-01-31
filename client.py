################################################################################
#
#  Permission is hereby granted, free of charge, to any person obtaining a
#  copy of this software and associated documentation files (the "Software"),
#  to deal in the Software without restriction, including without limitation
#  the rights to use, copy, modify, merge, publish, distribute, sublicense,
#  and/or sell copies of the Software, and to permit persons to whom the
#  Software is furnished to do so, subject to the following conditions:
#
#  The above copyright notice and this permission notice shall be included in
#  all copies or substantial portions of the Software.
#
#  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS
#  OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
#  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
#  DEALINGS IN THE SOFTWARE.

import urllib2
import time
import json
import random

# Server API URLs
QUERY = "http://localhost:8080/query?id={}"

# 500k server request
N = 100

prev_bid_price = 0
prev_ask_price = 0

def getDataPoint(quote):
	""" Produce all of the needed values to generate a datapoint """
	""" ------------- Update this function ------------- """
	global prev_bid_price
	global prev_ask_price
	stock = quote['stock']
	bid_price = 0
	bid_price_avg = 0
	ask_price = 0
	ask_price_avg = 0

	if quote['top_bid']:
		bid_price = float(quote['top_bid']['price'])
		bid_price_avg = (bid_price + prev_bid_price)/ 2
		prev_bid_price = bid_price

	if quote['top_ask']:
		ask_price = float(quote['top_ask']['price'])
		ask_price_avg = (ask_price + prev_ask_price)/ 2
		prev_ask_price = ask_price
	return stock, bid_price, bid_price_avg, ask_price, ask_price_avg

# Main
if __name__ == "__main__":

	# Query the price once every N seconds.
	for _ in xrange(N):
		quotes = json.loads(urllib2.urlopen(QUERY.format(random.random())).read())

		for quote in quotes:
			stock, bid_price, bid_price_avg, ask_price, ask_price_avg = getDataPoint(quote)
			print "Quoted %s at (bid:%s, avg bid:%s, ask:%s, avg ask:%s)" % (stock, bid_price, bid_price_avg, ask_price, ask_price_avg)
