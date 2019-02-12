<br>
<p align="center">
<a href="https://www.insidesherpa.com/virtual-internships/prototype/R5iK7HMxJGBgaSbvk/Technology%20Virtual%20Experience" target="_blank">
<img src="https://s3-ap-southeast-2.amazonaws.com/insidesherpa-assets/icons/promo_files/Screen+Shot+2019-02-11+at+11.32.13+pm.png"></a>
</p>

<br>
<p align="center"> 
	<b><a href="#task">Task Overview</a></b>
	|
	<b><a href="#installation">Installation Instructions</a></b>
	| 
	<b><a href="https://www.insidesherpa.com/modules/R5iK7HMxJGBgaSbvk/gtAhtcvke9AFCzqME" target="_blank">Link to Module 1</a></b>
	
</p>
<br>

<h1> Experience Technology at Bank&MergeCo. </h1> 
<p>Try out what real work is like in the technology team at Bank & Merge Co. Fast track to the tech team with your work.</p>

<br>

<h2 id="task"> Module 1 Task Overview </h2>
<p>Interface with a stock price data feed and set up your system for analysis of the data</p>
<p> <b>Aim:</b> We want to process the data feed of stock A and stock B’s price to enable us to analyse when trading for the stock should occur.</p>

<ol>
	<li>Please clone this repository to start the task</li>
	<li>Adjust the getRatio and getDataPoint functions</li>
	<li>Pass all unit tests and add more to cover edge cases</li>
	<li>Upload a git patch file as the submission to this task</li>
	
</ol>

<br>

<h2 id="installation" >Installation</h2>

Please ensure you are using <b> python2.7. </b>

Start the data feed server by running:

<code> python datafeed/server.py</code>

Run <code>npm install</code> to start the application.

To run the app in development mode, run <code>npm start</code> in the project directory.

Open http://localhost:3000 to view the app in the browser. The page will reload if you make edits.

<h2>Run</h2>
To start the server (this will create random market called 'test.csv' in your
working directory if one does not already exist):

	python server.py

To start the example client:

	python client.py

To unit test the example client:
	python client_test.py

<h2>API Examples</h2>

See also [client.py](https://github.com/texodus/exchange_simulator/blob/master/client.py)

Query:

	$ curl 'http://localhost:8080/query?id=1'
	{"id": "1", "top_ask": {"price": 129.18, "size": 70}, "timestamp": "2016-08-06 12:32:11.821574", "top_bid": {"price": 128.79, "size": 61}}
