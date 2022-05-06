from flask import Flask , request, jsonify, Response
from flask_restful import Resource , Api ,reqparse
from flask_cors import CORS
from bson import json_util
import pandas as pd

from flask_pymongo import PyMongo

app = Flask(__name__ )

app.config["MONGO_URI"] = "mongodb://Emanuele-Visioli:EMAnuele25102004@cluster0-shard-00-00.x7fma.mongodb.net:27017,cluster0-shard-00-01.x7fma.mongodb.net:27017,cluster0-shard-00-02.x7fma.mongodb.net:27017/Sanita?ssl=true&replicaSet=atlas-566dc8-shard-0&authSource=admin&retryWrites=true&w=majority" #bisogna anche specificare il nome del database al interno del link 

mongo = PyMongo(app)

CORS(app)
api = Api(app)


#-------------------------------------------------------------------------------------------------------------------Prova

class UsersApi(Resource):
    #def get(self):
    #    uss = mongo.db.medici_medicina_generale.find()
    #    resp = json_util.dumps(uss)
    #    return Response(resp, mimetype = 'application/json') 
    def post(self):
        user = request.json["user"]
        informatica = request.json["informatica"]
        matematica = request.json["matematica"]
        arte = request.json["arte"]
        if user and informatica and matematica and arte:
            id = mongo.db.Prova1.insert_one(
                {
                'user': user,
                'informatica': informatica,
                'matematica': matematica,
                'arte': arte 
                }
            )
            resp = {
                "id" : str(id),
                'user': user,
                'informatica': informatica,
                'matematica': matematica,
                'arte': arte 
            }
            return resp
        else:
            return {'message': 'received'}
    def delete(self):
        #resp = mongo.db.prova.delete_one( { "_id": ObjectId("6274ed1cc8f6c95a70e9902e") } )
        return Response("ciao")#resp.deleted_count, mimetype = 'application/json') 
api.add_resource(UsersApi, '/users')



if __name__ == '__main__':
    app.run()