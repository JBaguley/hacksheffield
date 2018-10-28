from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import datafier
import main
app = Flask(__name__)
CORS(app)

@app.route("/api/lookup", methods=["POST"])
def receiveData():
    with open("data2.txt", "a") as f:
        f.write(request.json["name"]+":"+str(datafier.main(request.json["data"]))+"\n")

    return jsonify(request.json)