# Import libraries
from flask import Flask, request, jsonify
from flask_cors import CORS

import numpy as np
import json
import pickle
import pandas as pd
from werkzeug.wrappers import response
import util
from waitress import serve

import logging
logging.basicConfig()
logger = logging.getLogger('waitress')
logger.setLevel(logging.DEBUG)

app = Flask(__name__)
CORS(app)

# Load the model
model = pickle.load(open('model_rf.pkl', 'rb'))


@app.route('/', methods=['GET'])
def home():
    res = app.response_class(
        mimetype="application/json",
        response=json.dumps({
            "message": "Hello Stranger"
        })
    )

    return res


@app.route('/api', methods=['POST'])
def predict():
    # Get the data from the POST request.
    data = request.get_json(force=True)
    df = util.to_dataframe(data)

    prediction = model.predict(df)
    output = prediction[0]

    return app.response_class(
        mimetype="application/json",
        response=json.dumps({
            "data": str(output)
        })
    )


if __name__ == '__main__':
    serve(app=app, host='0.0.0.0', port=5500)
