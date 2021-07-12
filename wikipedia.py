"""
    geosearch.py

    MediaWiki API Demos
    Demo of `Geosearch` module: Search for wiki pages nearby

    MIT License
"""

import requests

S = requests.Session()

URL = "https://en.wikipedia.org/w/api.php"

PARAMS = {
    "format": "json",
    "list": "geosearch",
    "gscoord": "48.864824|-2.334595",
    "gslimit": "10",
    "gsradius": "10000",
    "action": "query",
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PLACES = DATA["query"]["geosearch"]

for place in PLACES:
    print(place["title"])

print(PLACES)
