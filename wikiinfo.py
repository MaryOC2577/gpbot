"""
    get_info.py

    MediaWiki API Demos
    Demo of `Info` module: Send a GET request to display information about a page.

    MIT License
"""

import requests

S = requests.Session()

URL = "https://fr.wikipedia.org/w/api.php"

PARAMS = {
    "action": "query",
    "format": "json",
    "titles": "Tour Eiffel",
    "prop": "info",
    "inprop": "url|talkid",
}

R = S.get(url=URL, params=PARAMS)
DATA = R.json()

PAGES = DATA["query"]["pages"]

print(PAGES)

for k, v in PAGES.items():
    print(v["title"] + " : " + v["fullurl"])
