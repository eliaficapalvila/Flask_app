from flask_script import Manager
from fooApp.app import app
from flask import Flask
from flask_pymongo import PyMongo

manager = Manager(app)
app.config['DEBUG'] = True # Ensure debugger will load.

if __name__ == '__main__':
    manager.run()

app = Flask(__name__)

app.config['MONGO_DBNAME'] = 'foodb'
app.config['MONGO_URI'] = 'mongodb://localhost:27017/foodb'

mongo = PyMongo(app)
