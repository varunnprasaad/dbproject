from flask import make_response, jsonify, request

from db import db_handler
from . import app


@app.route('/')
def index():
    return make_response("Hello")


@app.route('/getcars')
def get_cars():
    cars = db_handler.db_get_cars()
    print(cars)
    return jsonify(cars)


@app.route('/getcarbycategory')
def get_car_by_category():
    category = request.args.get('category')
    cars = db_handler.db_get_cars_by_category(category)
    print(cars)
    return jsonify(cars)
