from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import datafier
app = Flask(__name__)
CORS(app)


@app.route("/api/lookup", methods=["POST"])
def receiveData():
    print(datafier.main(request.json["data"]))
    return jsonify(request.json)