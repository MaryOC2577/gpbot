import json

from flask import request
from flask.json import jsonify
from flask import render_template

from app.models.clean_sentence import Parser
from app.models.gps_coordinates import HereAPI
from app.models.clean_wiki import WikiAPI

from app import app


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/find_place", methods=["GET", "POST"])
def find_place():
    # --- A supprimer ---
    # res = request.get_json()
    # print(res)
    # clear_sentence = res["text"]
    # print("sentence : ", clear_sentence)
    # result = CleanSentence()
    # coords = HereGps()
    # wiki = WikiInfo()
    # place_coords = coords.find_coordinates(
    #     " ".join(result.clean_sentence(clear_sentence))
    # )
    # print("Cleaned sentence : ", " ".join(result.clean_sentence(clear_sentence)))
    # print("Coords : ", place_coords["coords"])
    # print("adress : ", place_coords["adress"])
    # print("Wiki info : ", wiki.clean_wiki(clear_sentence))
    # ---

    data = request.get_json()
    text = data["text"]

    parser = Parser()
    hereapi = HereAPI()
    wikiapi = WikiAPI()

    cleaned_text = parser.clean_text(text)
    print("cleaned text :", cleaned_text)
    coords = hereapi.find_coordinates(cleaned_text)
    print("coords :", coords)
    wiki_text = wikiapi.find_wiki_text(cleaned_text)
    print("wiki text :", wiki_text)

    return jsonify(
        # --- old ---
        # cleaned_text=res["text"],
        # place_lat=place_coords["coords"]["lat"],
        # place_lng=place_coords["coords"]["lng"],
        # place_adress=place_coords["adress"],
        # wiki_info=wiki.clean_wiki(clear_sentence),
        # --- end ---
        text=text,
        coords=coords,
        wiki_info=wiki_text,
    )
