import recommender

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
  return 'Hello World'

@app.route('/recommendation', methods=['POST'])
def recommend():
  results = recommender.recommend(request.args.get('request'))
  return jsonify(results),200