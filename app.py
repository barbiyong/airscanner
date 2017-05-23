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

flights_cache_service = FlightsCache('_Iw9z5pE5NoLEUezrLaEuLyp0KS_Y03FBbl9VogFh3I3uJ7CfXAzagNHrj9BAJubROPPJmWJYThLm5mPgJjQBxw==')

app = Flask(__name__, static_url_path='')

'''
Get Flights order by price.
'''
@app.route('/api/v1/flight/byprice', methods=["GET", "POST"])
def find_flight_by_price():
    flight_place = request.args.get('flight_place')

    result = flights_cache_service.get_cheapest_quotes(
        market='TH',
        currency='THB',
        locale='th-TH',
        originplace='BKKT',
        destinationplace=flight_place,
        outbounddate='2017-05',
        inbounddate='2017-06').parsed
    places = result['Places']
    quotes = result['Quotes']

    el = []
    for i in xrange(0,len(places)):
        if i >= 10:
            break
        el.append({
            "title": str(quotes[i]['MinPrice']) + ' ' + places[i]['Name'],
            "subtitle": u'ขาไป: ' + quotes[i]['OutboundLeg']['DepartureDate'],
            "buttons":[
            {
                "type":"web_url",
                "url":"http://whitelabeldemo.skyscanner.net/th-TH/flights/#/result?originplace=BKKT&destinationplace=OSAA&outbounddate=2017-05-26&inbounddate=2017-06-27&cabinclass=Economy&adults=1&children=0&infants=0",
                "title":"Buy Ticket"
            }
            ]
        })
    
    messages = {
        "messages": [
            {
                "attachment":{
                    "type":"template",
                    "payload":{
                        "template_type":"generic",
                        "elements": el
                    }
                }
            }
        ]
    }

    return jsonify(messages)

'''
Get Flights by route order by price
'''
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

    ''' assemble object '''

    return jsonify(result)

'''
Get Cheapest Hotel by airbnb
'''
@app.route('/api/v1/hotel/byprice', methods=["GET", "POST"])
def find_hotel_by_price():
    result = airbnb_get_places('bangkok')
    return jsonify(result)


AIRBNB_CONFIG = {
    'BASE_URL': "https://api.airbnb.com/v2/search_results",
    'CLIENT_ID': "?client_id=3092nxybyb0otqw18e8nh5nty"
}

def airbnb_get_places(location):
    request_ref = AIRBNB_CONFIG['BASE_URL'] + AIRBNB_CONFIG['CLIENT_ID'] + '&location' + '=' + location
    result = requests.get(request_ref).json()['search_results']
    el = []
    for r in result:
        el.append({
            picture_url: r['picture_url'],
            city: r['city'],
            name: r['name'],
            person_capacity: r['person_capacity'],
            property_type: r['property_type'],
            star_rating: r['star_rating'],
            price_currency: r['pricing_quote']['localized_currency'],
            price: r['pricing_quote']['localized_nightly_price']
        })

    return result.json()['search_results']

if __name__ == '__main__':
    app.run(debug=True)
