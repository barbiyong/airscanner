# -*- coding: utf-8 -*-
import os
import sys
import json
import requests
import re
import time
from flask import Flask, request, render_template, jsonify
import random
import urllib
import datetime
from skyscanner.skyscanner import FlightsCache

flights_cache_service = FlightsCache('8e28260becd3441ca4e865396e224e7d_ecilpojl_EC71481935CEBB7EAF661BC24940D01D')

app = Flask(__name__, static_url_path='')

@app.route('/api/v1/', methods=["GET"])
def api_function():
	return None

'''
Get Flights order by price.
'''
@app.route('/api/v1/flight/byprice', methods=["GET", "POST"])
def find_flight_by_price():
	flight_price = request.args.get('flight_price')

	result = flights_cache_service.get_cheapest_quotes(
    market='TH',
    currency='THB',
    locale='th-TH',
    originplace='TH-sky',
    destinationplace='KUL-sky',
    outbounddate='2017-05',
    inbounddate='2017-06').parsed
	print result

	''' filter by price '''
	
	return jsonify({'a': 'a'})

@app.route('/api/v1/flight/byplace', methods=["GET", "POST"])
def find_flight_by_place():
	flight_place = request.args.get('flight_place')

	result = flights_cache_service.get_cheapest_price_by_route(
    market='TH',
    currency='THB',
    locale='th-TH',
    originplace='TH-sky',
    destinationplace='KUL-sky',
    outbounddate='2017-05',
    inbounddate='2017-06').parsed
	print result

	''' assemble object '''

	return jsonify({'a': 'a'})

# @app.route

if __name__ == '__main__':
    app.run(debug=True)
