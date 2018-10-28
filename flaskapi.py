from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import datafier
import main
app = Flask(__name__)
CORS(app)

data1 = {'avgKP': 365.9, 'specKP': {'e': {'l': 313.0, ' ': 171.0, 'Enter': 337.0}, 'l': {'l': 158.0, 'o': 187.0}, 'o': {' ': 213.0, 'e': 215.0}, ' ': {'m': 166.0, 'n': 197.0, 'i': 146.0, 'j': 224.0}, 'm': {'y': 218.0, 'e': 155.0}, 'y': {' ': 147.0}, 'n': {'a': 155.0}, 'a': {'m': 136.0}, 'i': {'s': 193.0}, 's': {' ': 185.0}, 'j': {'o': 143.0}}, 'totTime': 3832, 'backs': 0, 'shifts': 0, 'caps': 0}

@app.route("/api/lookup", methods=["POST"])
def receiveData():
    main.save("joe", data1)
    
    print(datafier.main(request.json["data"]))
    print(str(main.check("joe", datafier.main(request.json["data"]))))
    return str(main.check("joe", datafier.main(request.json["data"])))