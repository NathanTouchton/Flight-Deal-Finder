from pprint import pprint
from os import environ
from requests import get

class Sheety():
    def __init__(self):
        self.sheety_endpoint = get(
            url=f"{environ['SHEETY_URL']}"
            )
        self.sheety_endpoint.raise_for_status()
        self.sheet_data = self.sheety_endpoint.json()["prices"]

    def print_data(self):
        pprint(self.sheet_data)
