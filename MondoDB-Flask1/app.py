from flask import Flask , request, jsonify, Response
from flask_restful import Resource , Api ,reqparse
from flask_cors import CORS
import pandas as pd
from flask_pymongo import PyMongo

app = Flask(__name__)
app.config["MONGO_URI"] = 'mongodb://Livera2003:Waduge78&@cluster0-shard-00-00.uylmr.mongodb.net:27017,cluster0-shard-00-01.uylmr.mongodb.net:27017,cluster0-shard-00-02.uylmr.mongodb.net:27017/Livera1?ssl=true&replicaSet=atlas-38dmxu-shard-0&authSource=admin&retryWrites=true&w=majority'
mongo = PyMongo(app)
CORS(app)
api = Api(app)

class UsersApi(Resource):
    def get(self):
        uss = mongo.db.testdata.find()
        resp = json_util.dumps(uss)
        return Response(resp, mimetype = 'application/json') 
    '''def post(self):
        user = request.json["user"]
        nome = request.json["nome"]
        cognome = request.json["cognome"]
        telefono = request.json["telefono"]
        email = request.json["email"]
        data = request.json["data"]
        if user and nome and cognome and telefono and email and data:
            id = mongo.db.testdata.insert_one(
                {
                'user': user,
                'nome': nome,
                'cognome': cognome,
                'telefono': telefono,
                'email':email,
                'data':data
                }
            )
            resp = {
                "id" : str(id),
                'user': user,
                'nome': nome,
                'cognome': cognome,
                'telefono': telefono,
                'email':email,
                'data':data
            }
            return resp
        else:
            return {'message': 'received'}'''

api.add_resource(UsersApi, '/appuntamenti')


if __name__ == '__main__':
    app.run()