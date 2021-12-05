# Import libraries
from flask import Flask, request, jsonify
from flask_cors import CORS

import numpy as np
import json
import pickle
import pandas as pd
import util

app = Flask(__name__)
CORS(app)

# Load the model
model = pickle.load(open('model_rf.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    res = app.response_class(
        mimetype="application/json",
        response=json.dumps({
            "messagge": "Hello Stranger"
        })
    )

    return res


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)

    util.to_dataframe(data)
    return jsonify(str("HELLO"))


if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5500)
