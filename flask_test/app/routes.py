#!/usr/bin/env python3
from flask import render_template
from flask import jsonify
from app import app
import numpy as np

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/welcome')
def welcome():
    return "Hello, World! Greetings from HackAZ 2020!"

@app.route('/<float:lat>/<float:long>')
def get_percent(lat,long):
    placeholder = (lat+long)
    placeholder_data = list(zip(list(np.linspace(0,100,25)),list(np.linspace(-118.7,-110.8,25))))
    d = {'percent':placeholder, 'paths':placeholder_data}
    return jsonify(d)
