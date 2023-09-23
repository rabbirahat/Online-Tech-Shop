from flask import Flask, render_template,request

app = Flask(__name__)
import pymongo
db_client = pymongo.MongoClient("mongodb://localhost:27017")
# db = db_client["students"]
# mark_table = db["mark"]

db = db_client.test_db
test_collection = db.test_collection
test_collection2 = db.test_collection2

from shop import routes
