<h1>Installation</h1>

python datafeed/server.py
Before you can start this application, you have to run

npm install
In the project directory, you can run:

npm start
Runs the app in the development mode.
Open http://localhost:3000 to view it in the browser.

The page will reload if you make edits.

Run
===
To start the server (this will create random market called 'test.csv' in your
working directory if one does not already exist):

	python server.py

To start the example client:

	python client.py

To unit test the example client:
	python client_test.py

API Examples
============
See also [client.py](https://github.com/texodus/exchange_simulator/blob/master/client.py)

Query:

	$ curl 'http://localhost:8080/query?id=1'
	{"id": "1", "top_ask": {"price": 129.18, "size": 70}, "timestamp": "2016-08-06 12:32:11.821574", "top_bid": {"price": 128.79, "size": 61}}
