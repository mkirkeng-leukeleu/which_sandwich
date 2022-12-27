from flask import Flask, jsonify, abort, request
from flask_cors import CORS, cross_origin
import time
from datetime import datetime as dt
from pprint import pprint as pp

SIM_DELAY = 0.3
EXAMPLE_DATA = True

datetime_format = "%Y-%m-%d %H:%M:%S"
def get_datetime():
    return dt.now().strftime(datetime_format)

example_data = [
    {'breadType': 'brown',
    'date': dt(2022, 12, 23, 13, 8, 35, 838791),
    'email': 'kermit@gmail.com',
    'sandwich': 'oldCheeseSandwich'},
    {'breadType': 'brown',
    'date': dt(2022, 12, 23, 13, 13, 12, 99717),
    'email': 'kermit@gmail.com',
    'sandwich': 'youngCheeseSandwich'},
    {'breadType': 'brown',
    'date': dt(2022, 12, 23, 13, 13, 49, 392231),
    'email': 'mkirkeng@leukeleu.nl',
    'sandwich': 'youngCheeseSandwich'},
    {'breadType': 'brown',
    'date': dt(2022, 12, 9, 13, 15, 29, 305024),
    'email': 'mkirkeng@leukeleu.nl',
    'sandwich': 'humusSandwich'},
    {'breadType': 'brown',
    'date': dt(2022, 12, 20, 13, 15, 29, 305024),
    'email': 'obama@leukeleu.nl',
    'sandwich': 'humusSandwich'},
    {'breadType': 'brown',
    'date': dt(2022, 12, 13, 13, 15, 29, 305024),
    'email': 'thehulk@leukeleu.nl',
    'sandwich': 'humusSandwich'}
]
db = example_data if EXAMPLE_DATA else []

app = Flask(__name__)
app.debug = True
CORS(app)

def serialize_order(order_obj):
    res = {**order_obj, 'date': order_obj['date'].strftime(datetime_format)}
    return res

@app.route('/', methods=["GET"])
@cross_origin()
def index():
    return "<h1>Welcome to my temporary API</h1>"

@app.route('/orders', methods=["GET", "POST"])
@cross_origin()
def orders():
    global db

    if request.method == "GET":
        if not db:
            return jsonify([]), 200

        if "today" in request.args:
            today = dt.now().date()
            todays_orders = [order for order in db if order['date'].date() == today]
            todays_orders.sort(key=lambda x: x.get('date'))

            if todays_orders:
                return serialize_order(todays_orders[-1]), 200
            else:
                return jsonify([])
                

        return jsonify([serialize_order(order) for order in db]), 200
    elif request.method == "POST":
        order = request.json
        order["date"] = dt.now()
        db.append(order)
        
        return jsonify(serialize_order(order)), 201

@app.after_request
def add_header(response):
    # avoid cors errors
    response.headers['Access-Control-Allow-Origin'] = '*'
    
    # simulate a slow network
    time.sleep(SIM_DELAY)

    return response

if __name__ == "__main__":
    app.run(host='localhost', port=5000)
