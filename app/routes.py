import json
from flask import request
from flask.helpers import make_response
from flask.json import jsonify
from app import app
from flask import render_template
from app.models.clean_sentence import CleanSentence
from app.models.gps_coordinates import HereGps


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/find_place", methods=["POST"])
def find_place():
    res = request.get_json()
    clear_sentence = res["text"]
    print("sentence : ", clear_sentence)
    result = CleanSentence()
    coords = HereGps()
    place_coords = coords.find_coordinates(
        " ".join(result.clean_sentence(clear_sentence))
    )
    print("Coords : ", place_coords)
    return jsonify(
        cleaned_text=res["text"],
        place_lng=place_coords["lng"],
        place_lat=place_coords["lat"],
    )
