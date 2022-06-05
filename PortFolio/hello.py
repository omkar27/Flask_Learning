from flask import Flask
import requests
from markupsafe import escape
import json

app = Flask(__name__)

@app.route("/")
def index():
    return test_api()

@app.route("/<name>")
def hello_world(name):
    return f"<p>Hello, {escape(name)}</p>"

def test_api():
	response = requests.get("https://jsonplaceholder.typicode.com/todos/1")
	print(response.status_code)
	return json.loads(response.text)	