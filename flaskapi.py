from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import datafier
import main
app = Flask(__name__)
CORS(app)

data1 = {'avgKP': 381.6363636363636, 'specKP': {'h': {'e': 116.0}, 'e': {'l': 298.0, ' ': 103.0, 'Enter': 1144.0}, 'l': {'l': 129.0, 'o': 199.0}, 'o': {' ': 149.0, 'e': 133.0}, ' ': {'m': 198.0, 'n': 206.0, 'i': 193.0, 'j': 214.0}, 'm': {'y': 267.0, 'e': 139.0}, 'y': {' ': 77.0}, 'n': {'a': 103.0}, 'a': {'m': 128.0}, 'i': {'s': 134.0}, 's': {' ': 148.0}, 'j': {'o': 120.0}}, 'totTime': 4198, 'backs': 0, 'shifts': 0, 'caps': 0}

@app.route("/api/lookup", methods=["POST"])
def receiveData():
    main.save("joe", data1)
    main.check("joe", datafier.main(request.json["data"]))
    #print(datafier.main(request.json["data"]))
    return jsonify(request.json)