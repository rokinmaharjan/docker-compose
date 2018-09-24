from flask import Flask

from flask_pymongo import PyMongo
from bson.json_util import dumps

app = Flask(__name__)
app.config["MONGO_URI"] = "mongodb://database:27017/local"
mongo = PyMongo(app)

@app.route("/")
def home_page():
    mongo.db.users.insert_one({'name': 'Rokin'})
    
    return dumps(mongo.db.users.find())

@app.route("/test")
def test():
    return "works"