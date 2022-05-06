from flask_pymongo import PyMongo
import flask

app = flask.Flask(__name__)

mongodb_client = PyMongo(app, uri="mongodb://localhost:27017/Livera1")
db = mongodb_client.db

@app.route("/add_many")
def add_many():
    db.testdata.insert_many([
        {'_id': 1, 'title': "todo title one ", 'body': "todo body one "},
        {'_id': 2, 'title': "todo title two", 'body': "todo body two"},
        {'_id': 3, 'title': "todo title three", 'body': "todo body three"},
        {'_id': 4, 'title': "todo title four", 'body': "todo body four"},
        {'_id': 5, 'title': "todo title five", 'body': "todo body five"},
        {'_id': 1, 'title': "todo title six", 'body': "todo body six"},
        ])
    return flask.jsonify(message="success")

if __name__ == '__main__':
    app.run()