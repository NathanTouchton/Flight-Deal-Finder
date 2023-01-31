from os import environ
from requests import get
from data_manager import Sheety

# SHEETY_DATA = Sheety()
# SHEETY_DATA.print_data()

TEQUILA_HEADER = {
    "apikey": environ["TEQUILA_KEY"],
}

class FlightSearch():
    def __init__(self):
        self.tequila_endpoint = get(
            "https://api.tequila.kiwi.com/v2/search",
            headers=TEQUILA_HEADER
            )
        self.tequila_endpoint.raise_for_status()
