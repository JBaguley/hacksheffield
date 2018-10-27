from flask import Flask, request, jsonify
from flask_cors import CORS
import json
app = Flask(__name__)
CORS(app)


@app.route("/api/lookup", methods=["POST"])
def receiveData():
    return jsonify(request.json)