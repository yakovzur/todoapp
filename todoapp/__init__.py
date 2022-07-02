from flask import Flask

from .extensions import mongo

from .main.routes import main

from dotenv import load_dotenv

import os

def create_app():
    app = Flask(__name__)

    load_dotenv()

    app.config['MONGO_URI'] = 'mongodb+srv://yaki:3963@loe.jwuon.mongodb.net/mydb?retryWrites=true&w=majority'

    mongo.init_app(app)

    app.register_blueprint(main)

    return app