import requests
import json


def initial_api(config):
    return AirBnbPy(config)


class AirBnbPy():
    """ AirBnbPy Interfaces """

    def __init__(config):
        self.BASE_URL = "https://api.airbnb.com/v2/search_results"
        self.API_SERVICES_URL = ""
        self.DEFAULT_CLIENT_ID = "?client_id=3092nxybyb0otqw18e8nh5nty"
        self.apiKey = config['API_KEY']

    def get_countries(locale):
        request_ref = self.BASE_URL + self.DEFAULT_CLIENT_ID + '&locale' + '=' + locale
        pass

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

    def get_browserquotes():
        """
        /browsequotes/v1.0/
        {_format}/
        {currency}/
        {locale}/
        {location}/
        {guests}/
        {price_max}/
        {checkin}/
        {checkout}/
        {inboundPartialDate} <- Optimal
        """
        pass
