from flask import Flask
from flask_cors import CORS
import json
import pandas as pd
from analitics import *

DF = pd.read_json('ventas.json')

app = Flask(__name__)
CORS(app)


@app.route('/route_get_time_spent_by_day', methods=['GET'])
def route_get_time_spent_by_day():
    return json.loads(get_time_spent_by_day(DF))


@app.route('/route_get_money_spent_by_day', methods=['GET'])
def route_get_money_spent_by_day():
    return json.loads(get_money_spent_by_day(DF))


@app.route('/route_get_total_dinners_by_day', methods=['GET'])
def route_get_total_dinners_by_day():
    return json.loads(get_total_dinners_by_day(DF))


@app.route('/route_get_effective_work_by_waiter', methods=['GET'])
def route_get_effective_work_by_waiter():
    return json.loads(get_effective_work_by_waiter(DF))


@app.route('/route_get_effective_work_by_cashier', methods=['GET'])
def route_get_effective_work_by_cashier():
    return json.loads(get_effective_work_by_cashier(DF))


if __name__ == '__main__':
    app.run(debug=True)