# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,jsonify, make_response
from flask_restful import Resource,Api
from predictiveScore import result
import json
app = Flask(__name__)
item = []
api = Api(app)
class Item(Resource):
    def __init__(self):
        self.x = result()
        
    def post(self):
        return jsonify(self.x),201



api.add_resource(Item,'/get_score')
app.run(port=5000, debug=True)

