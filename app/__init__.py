from flask import Flask
import main
app =  Flask(__name__)

@app.route("/")
def hello():
	print main.evaluate(["What is the capital of India"])
        return "Hello World"
