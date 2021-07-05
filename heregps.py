import requests
from pprint import pprint

url = "https://geocode.search.hereapi.com/v1/geocode"
params = {
    "apiKey": "nA_2GT2YF3clqlab3lCR8BNVlyVeSdcnmZ2Co_6d9VE",
    "q": "statue de la liberté",
}

response = requests.get(url, params=params)
pprint(response.json())
coord = response.json()["items"][0]["position"]
print("GPS Coordinates : ", coord)
