from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import datafier
import main
app = Flask(__name__)
CORS(app)

data1 = {'avgKP': 290.5, 'specKP': {'H': {'e': 186.0}, 'e': {'l': 143.0, ' ': 97.0, 'Enter': 170.0}, 'l': {'l': 477.0, 'o': 187.0}, 'o': {' ': 222.0, 'e': 134.0}, ' ': {'m': 245.0, 'n': 212.0, 'i': 120.0, 'Shift': 127.0}, 'm': {'y': 232.0, 'e': 119.0}, 'y': {' ': 93.0}, 'n': {'a': 138.0}, 'a': {'m': 108.0}, 'i': {'s': 104.0}, 's': {' ': 107.0}, 'Shift': {'J': 90.0}, 'J': {'o': 175.0}}, 'totTime': 3695, 'backs': 0, 'shifts': 2, 'caps': 0}

@app.route("/api/lookup", methods=["POST"])
def receiveData():
    main.save("joe", data1)
    
    print(datafier.main(request.json["data"]))
    print(str(main.check("joe", datafier.main(request.json["data"]))))
    return str(main.check("joe", datafier.main(request.json["data"])))