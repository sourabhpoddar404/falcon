import json
from flask import Flask
from flask import request
import main
app =  Flask(__name__)

@app.route("/", methods=['POST'])
def hello():
    question = request.json['text']
    result = list(main.evaluate([question]))
    print(result)
    relations = result[2]
    entities = result[3]
    response = {
        "relations_dbpedia" : relations,
        "entities_dbpedia" : entities
    }
    resposnejson = json.dumps(response)
    return resposnejson

