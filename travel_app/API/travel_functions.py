import amadeus 
import json
import requests
from API.config import base_url, token_headers, token_url
from API.creds import api_key, api_secret


def api_login():
    """This function logs into the API and returns a token."""
    amadeus = amadeus.Client(
        client_id=api_key,
        client_secret=api_secret
    )

    try:
        response = amadeus.shopping.flight_dates.get(origin='ORD', destination='LAX')
        print(response.data)
    except amadeus.ResponseError as error:
        print(error)


def retrieve_travel_info(source, destination, start_date, end_date, headers):
    """This functions calls the API and returns flight information based on the arguments."""
    pass
    

def list_trip_options(api_response):
    """Function which parses API response and returns top 5 list of airfare choices based on price."""
    pass