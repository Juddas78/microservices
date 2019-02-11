from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

VERSION = "0.1"

@app.route('/')
def version():
	return jsonify(version=VERSION)


