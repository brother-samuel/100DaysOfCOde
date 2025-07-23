import os
import requests
from pprint import pprint
from dotenv import load_dotenv

load_dotenv()

SHEETY_ENDPOINT = "https://api.sheety.co/120efa0f56cfd0819e0410e6c9a99386/flightDeals/prices"
BEARER = os.getenv('BEARER')
SHEETY_HEADER = {'Authorization': f"Bearer {BEARER}"}

class DataManager:

    def __init__(self):
        self.destinations = {}


    def pull_destinations(self):
        response = requests.get(url=SHEETY_ENDPOINT, headers=SHEETY_HEADER)
        response.raise_for_status()
        data = response.json()
        self.destinations = data["prices"]
        return self.destinations
        # pprint(self.prices)

    def update_iata_code(self, code, row_id):
        update_endpoint = f"{SHEETY_ENDPOINT}/{row_id}"
        code_update = {
            "price": {
                'iataCode': code,
                 }
             }
        response = requests.put(url=update_endpoint, json=code_update ,headers=SHEETY_HEADER)
        print(response.text)
