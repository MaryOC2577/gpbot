"""Class that returns gps coordinates from a place name."""

import requests
from pprint import pprint


class HereAPI:
    def find_coordinates(self, sentence):

        url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {
            "apiKey": "nA_2GT2YF3clqlab3lCR8BNVlyVeSdcnmZ2Co_6d9VE",
            "q": sentence,
        }
        coords = {}
        response = requests.get(url, params=params)
        if response.json()["items"] == []:
            coords = {"coords": {"lat": 43.29337, "lng": 5.37131}}
        else:
            coords["coords"] = response.json()["items"][0]["position"]
            coords["adress"] = response.json()["items"][0]["title"]
        return coords
