"""Class that returns gps coordinates from a place name."""

import requests

import os


class HereAPI:
    def find_coordinates(self, sentence):
        """Return coords of a location."""

        url = "https://geocode.search.hereapi.com/v1/geocode"
        params = {
            "apiKey": os.getenv("API_KEY"),
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
