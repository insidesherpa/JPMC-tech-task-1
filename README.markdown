<p align="center">
<a href="https://www.insidesherpa.com/virtual-internships/prototype/R5iK7HMxJGBgaSbvk/Technology%20Virtual%20Experience" target="_blank">
<img src="https://s3-ap-southeast-2.amazonaws.com/insidesherpa-assets/icons/promo_files/Screen+Shot+2019-02-11+at+11.32.13+pm.png"></a>
</p>

<p align="center"> 
	<b><a href="https://www.insidesherpa.com/modules/R5iK7HMxJGBgaSbvk/gtAhtcvke9AFCzqME" target="_blank">Module 1</a></b>
	| 
	<b><a href="#task">Task Overview</a></b>
	|
	<b><a href="#installation">Installation Instructions</a></b>
</p>


<h1> Experience Technology at Bank&MergeCo. </h1> 


Interface with a stock price data feed and set up your system for analysis of the data

<br>

<h2 id="task"> Module 1 Task Overview </h2>
<p>Interface with a stock price data feed and set up your system for analysis of the data</p>
<p> We want to process the data feed of stock A and stock B’s price to enable us to analyse when trading for the stock should occur.</p>

<ol>
	<li>Please clone this repository to start the task</li>
	<li>Adjust the getRatio and getDataPoint functions</li>
	<li>Pass all unit tests and add more to cover edge cases</li>
	<li>Upload a git patch file as the submission to this task</li>
	
</ol>

<br>

<h2 id="installation" >Installation</h2>

please start the data feed server by running

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
