import json
from flask import request
from flask.helpers import make_response
from flask.json import jsonify
from app import app
from flask import render_template

# from app.models.clean_sentence import CleanSentence


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/json")
def get_bot_response():
    return render_template("get_bot_response.json")


@app.route("/find_place", methods=["POST"])
def find_place():
    res = request.get_json()
    print("sentence : ", res["text"])
    # result = CleanSentence.clean_sentence(res)
    # print("cleaned sentence : ", result)
    return jsonify(cleaned_text=res["text"])
