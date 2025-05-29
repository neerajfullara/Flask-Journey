from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<h1>Hello World</h1>"

@app.route("/home")
def home():
    return "<h1>This the home.</h1?"

@app.route("/json")
def json():
    return {
        "My Key": "JSON Value"
    }