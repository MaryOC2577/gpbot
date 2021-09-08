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
    """Show home page."""
    return render_template("index.html", title="Home")


@app.route("/find_place", methods=["GET", "POST"])
def find_place():
    """Show infos about a location."""

    data = request.get_json()
    text = data["text"]

    parser = Parser()
    hereapi = HereAPI()
    wikiapi = WikiAPI()

    cleaned_text = parser.clean_text(text)
    print("cleaned text :", cleaned_text)
    coords = hereapi.find_coordinates(cleaned_text)
    print("coords :", coords)
    wiki_text = wikiapi.get_text(cleaned_text)
    print("wiki text :", wiki_text)

    return jsonify(
        text=text,
        coords=coords,
        wiki_info=wiki_text,
    )
