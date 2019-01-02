
"""
Spyder Editor

This is a temporary script file.
"""
from flask import Flask,jsonify, make_response
from flask_restful import Resource,Api
from predictiveScore import result

app = Flask(__name__)
item = []
api = Api(app)
class Item(Resource):
    def get(self,name):
        x = result(name)
        return jsonify(x)



api.add_resource(Item,'/get_score/<string:name>')
app.run(host = '127.0.0.2',debug=True)

