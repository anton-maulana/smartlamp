import sys
sys.path.append("../")
sys.path.append("../common")

from flask import Blueprint, jsonify, current_app
from repository import PinOutRepository
from common.database import db
from time import time


app = Blueprint('switch', __name__)
region_repository = PinOutRepository(db)

@app.route('/switch', methods=['GET'])
def fetch_desas():
    region_repository.all()
    return "hello"

