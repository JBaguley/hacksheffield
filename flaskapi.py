from flask import Flask, request, jsonify
import json
app = Flask(__name__)


@app.route("/api/lookup", methods=["POST"])
def receiveData():
    return jsonify(request.json)