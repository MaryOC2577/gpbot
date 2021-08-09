import json

from flask import request
from flask.helpers import make_response
from flask.json import jsonify
from flask import render_template

from app.models.clean_sentence import CleanSentence
from app.models.gps_coordinates import HereGps
from app.models.clean_wiki import WikiInfo

from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/find_place", methods=["GET", "POST"])
def find_place():
    
    # ----
#     res = request.get_json()
#     print(res)
#     clear_sentence = res["text"]
#     print("sentence : ", clear_sentence)
#     result = CleanSentence()
#     coords = HereGps()
#     wiki = WikiInfo()
#     place_coords = coords.find_coordinates(
#         " ".join(result.clean_sentence(clear_sentence))
#     )
#     print("Cleaned sentence : ", " ".join(result.clean_sentence(clear_sentence)))
#     print("Coords : ", place_coords["coords"])
#     print("adress : ", place_coords["adress"])
#     print("Wiki info : ", wiki.clean_wiki(clear_sentence))
    
    # ----
    # attention ici j'ai renommé les méthodes et les objets :)
    data = request.get_json()
    text = data["text"]
 
    parser = Parser()
    herapi = HereAPI()
    wikiapi = WikiAPI()
 
    cleaned_text = parser.clean_text(text)  # devrait retourner du texte sous forme de string ;)
    coords = hereapi.find_coordinates(cleaned_text)
    wiki_text = wikiapi.find_wiki_text(cleaned_text)

    return jsonify(
        text=text,
        coords=coords, # traitement de lat, long et adress dans le js directement ;)
        wiki_info=wiki_text,
    )
