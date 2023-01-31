from pprint import pprint
from requests import get

class Sheety():
    def __init__(self):
        self.sheety_endpoint = get(
            url="https://api.sheety.co/73adde8dc51c874d56a66ff4e6643923/flightDeals/prices"
            )
        self.sheety_endpoint.raise_for_status()
        self.sheet_data = self.sheety_endpoint.json()["prices"]

    def print_data(self):
        pprint(self.sheet_data)
