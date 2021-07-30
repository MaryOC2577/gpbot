"""Class that returns gps coordinates from a place name."""

import requests
from pprint import pprint


class HereGps:
    def find_coordinates(self, sentence):

        url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {
            "apiKey": "nA_2GT2YF3clqlab3lCR8BNVlyVeSdcnmZ2Co_6d9VE",
            "q": sentence,
        }
        coords = {}
        response = requests.get(url, params=params)
        coords["coords"] = response.json()["items"][0]["position"]
        # print("adresse : ", response.json()["items"][0]["title"])
        coords["adress"] = response.json()["items"][0]["title"]
        # print("adress : ", coords["adress"])
        return coords
