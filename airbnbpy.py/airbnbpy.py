import requests
import json


def initial_api(config):
	return AirBnbPy(config)


class AirBnbPy():
	""" AirBnbPy Interfaces """
	def __init__(config):
		self.BASE_URL = ""
		self.API_SERVICES_URL = ""
		self.apiKey = config['API_KEY']
