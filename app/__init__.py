import json
from flask import Flask
import main
app =  Flask(__name__)

@app.route("/")
def hello():
    result = main.evaluate(["What is the capital of India"])
    relations = result[2]
    response = {
        "relations_dbpedia" : relations
    }
    resposnejson = json.loads(response)
    return resposnejson

