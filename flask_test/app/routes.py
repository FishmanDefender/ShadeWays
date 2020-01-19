#!/usr/bin/env python3
from flask import render_template
from flask import jsonify
from app import app
import numpy as np
from main import main

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    return render_template('index.html', title='Home', user=user)


@app.route('/welcome')
def welcome():
    return "Hello, World! Greetings from HackAZ 2020!"

@app.route('/<float:lat1>/<float:long1>/<float:lat2>/<float:long2>/')
def get_percent(lat1,long1,lat2,long2):
    percent, google_query = main((lat1,long1),(lat2,long2))
    d = {'percent':percent, 'google_api':google_query}
    return jsonify(d)
