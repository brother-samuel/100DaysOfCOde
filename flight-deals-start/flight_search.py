import os
from pprint import pprint
import requests
import datetime as dt
from dotenv import load_dotenv

load_dotenv()

class FlightSearch:
    #This class is responsible for talking to the Flight Search API.
    def __init__(self):
        self._api_key = os.getenv("AMADEUS-API")
        self._api_secret = os.getenv("AMADEUS-SECRET")
        self._token = self.get_new_token()

    def get_new_token(self):
        token_endpoint = "https://test.api.amadeus.com/v1/security/oauth2/token"
        header = {
            'Content-Type': "application/x-www-form-urlencoded",
        }
        body = {
            'grant_type': 'client_credentials',
            'client_id': self._api_key,
            'client_secret': self._api_secret,
        }
        response = requests.post(url=token_endpoint, headers=header, data=body)
        return response.json()['access_token']

    def pull_iata_code(self, city_name):
        city_search_endpoint = "https://test.api.amadeus.com/v1/reference-data/locations/cities"
        header = {"Authorization": f"Bearer {self._token}"}
        query = {
            "keyword": city_name,
            "max": "2",
            "include": "AIRPORTS",
        }
        response = requests.get(url=city_search_endpoint, headers=header, params=query)
        response.raise_for_status()
        # print(response.text)
        code = response.json()['data'][0]['iataCode']
        return code

    def search_flights(self, destination, max_price):
        today = dt.datetime.today()
        flight_search_endpoint = "https://test.api.amadeus.com/v2/shopping/flight-offers"
        header = {"Authorization": f"Bearer {self._token}"}
        query = {
            'originLocationCode': 'PRG',
            'destinationLocationCode': destination,
            'departureDate': "2025-07-22",
            'adults': 1,
            'maxPrice': max_price,
        }
        response = requests.get(url=flight_search_endpoint, headers=header, params=query)
        result = response.json()
        pprint(result)