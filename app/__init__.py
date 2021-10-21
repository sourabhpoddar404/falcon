import json
from flask import Flask
import main
app =  Flask(__name__)

@app.route("/")
def hello():
    result = list(main.evaluate(["What is the capital of India"]))
    relations = result[2]
    response = {
        "relations_dbpedia" : json.dump(relations)
    }
    resposnejson = json.dumps(response)
    return resposnejson

