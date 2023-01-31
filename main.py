from pprint import pprint
from os import environ
from requests import get, put
from twilio.rest import Client
from data_manager import Sheety

# TODO 1: Check for flight prices.
# TODO 2: Compare against prices on Google Sheet.
# TODO 3: Send text if price is under the threshold.
    # TODO 3.1: The SMS should include the departure airport IATA code, destination airport IATA code, departure city, destination city, flight price and flight dates.

# SHEETY_DATA = Sheety()

# TWILIO_SID = environ["TWILIO_SID"]
# TWILIO_KEY = environ["TWILIO_KEY"]

# message = client.messages.create(
#   body="Hello from Twilio",
#   from_="+19894742866",
#   to="+12244062483"
# )

# SHEETY_DATA.print_data()
