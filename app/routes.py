import json
from flask import request
from flask.helpers import make_response
from flask.json import jsonify
from app import app
from flask import render_template
from app.models.clean_sentence import CleanSentence


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
    result.clean_sentence(clear_sentence)
    print("cleaned sentence : ", result)
    return jsonify(cleaned_text=res["text"])
