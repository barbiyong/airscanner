import requests
import json


def initial_api(config):
	return Skypy(config)

class Skypy:
	""" SkyPy Interface """
	def __init__(self, config):
		self.BASE_URL = "http://partners.api.skyscanner.net"
		self.API_SERVICES_URL = "/apiservices/reference/v1.0"
		self.apiKey = config['API_KEY']

	def get_countries(locale):
		request_ref = self.BASE_URL + self.API_SERVICES_URL + '/countries' + '/' + locale
    pass

	def get_currencies():
		pass
	
	def get_places():
		pass
	
	def get_browserquotes()
		"""
		/browsequotes/v1.0/
		{country}/
		{currency}/
		{locale}/
		{originPlace}/
		{destinationPlace}/
		{outboundPartialDate}/
		{inboundPartialDate} <- Optimal
		"""
		pass



