import json
from flask import request
from flask.helpers import make_response
from flask.json import jsonify

from flask_cors.decorator import cross_origin
from app import app
from flask import render_template
from app.models.clean_sentence import CleanSentence
from app.models.gps_coordinates import HereGps
from app.models.clean_wiki import WikiInfo

from flask_cors import CORS

CORS(app)
cors = CORS(app, resources={r"/*": {"origins": "localhost"}})


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/find_place", methods=["GET", "POST"])
@cross_origin()
def find_place():
    res = request.get_json()
    print(res)
    clear_sentence = res["text"]
    print("sentence : ", clear_sentence)
    result = CleanSentence()
    coords = HereGps()
    wiki = WikiInfo()
    place_coords = coords.find_coordinates(
        " ".join(result.clean_sentence(clear_sentence))
    )
    print("Cleaned sentence : ", " ".join(result.clean_sentence(clear_sentence)))
    print("Coords : ", place_coords)
    print("Wiki info : ", wiki.clean_wiki(clear_sentence))
    return jsonify(
        cleaned_text=res["text"],
        place_lat=place_coords["lat"],
        place_lng=place_coords["lng"],
        wiki_info=wiki.clean_wiki(clear_sentence),
    )
