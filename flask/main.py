from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
import time
from datetime import datetime

SIM_DELAY = 0.3

def get_datetime():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

# db = {
#     "date": get_datetime(),
#     "email": "kermit@gmail.com",
#     "sandwich": "humusSandwich",
#     "breadType": "brown" 
# }
db = {}

app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/', methods=["GET"])
@cross_origin()
def index():
    return "<h1>Welcome to my temporary API</h1>"

@app.route('/order', methods=["GET", "POST"])
@cross_origin()
def order():
    global db

    if request.method == "GET":
        return jsonify(db), 200
    elif request.method == "POST":
        order = request.json
        order["date"] = get_datetime()
        db = order

        return jsonify(order), 201

@app.after_request
def add_header(response):
    # avoid cors errors
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    # simulate a slow network
    time.sleep(SIM_DELAY)

    return response

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
