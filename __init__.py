import sys
import os
import logging

from flask import Flask
from flask_cors import CORS
from controllers import *
from .common.database import db
from .common.marshmallow import ma

def create_app():
    app = Flask('smartlamp')

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

    app.register_blueprint(SwitchController)
    app.register_blueprint(PinOutController)

    db.init_app(app)
    ma.init_app(app)
    CORS(app)

    with app.app_context():
        # bind=None means that only main database is auto-created
        db.create_all()

    return app
