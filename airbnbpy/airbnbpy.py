import requests
import json


def initial_api():
    return AirBnbPy()


class AirBnbPy:
    """ AirBnbPy Interfaces """

    def __init__(self):
        self.BASE_URL = "https://api.airbnb.com/v2/search_results"
        self.DEFAULT_CLIENT_ID = "?client_id=3092nxybyb0otqw18e8nh5nty"
        self.apiKey = "915pw2pnf4h1aiguhph5gc5b2"

    def get_places(location):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&location' + '=' + location
        result = requests.get(request_ref)
        print result
        return result

    def get_currencies(currency):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&currency' + '=' + currency
        pass

    def get_places(location):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&location' + '=' + location
        pass

    def get_format(_format):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&_format' + '=' + 'for_search_results_with_minimal_pricing'
        pass

    def get_guest(guests):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&guests' + '=' + guests
        pass

    def get_price_max(price_max):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&price_max' + '=' + price_max
        pass

    def get_checkin(checkin):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&checkin' + '=' + checkin
        pass

    def get_checkin(checkout):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&checkout' + '=' + checkout
        pass

    def get_instant_bookable(ib):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&ib' + '=' + ib
        pass

