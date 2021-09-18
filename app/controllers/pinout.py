from flask import Blueprint, jsonify, request, current_app
from marshmallow import INCLUDE
from app.repository import PinOutRepository
from app import db
from app.helpers import ResponseHelper
from time import time
from app.models import PinOut, PinOutSchema
from marshmallow import ValidationError

app = Blueprint('pinout', __name__)
pinOutRepository = PinOutRepository(db)

@app.route('/pinout', methods=['GET'])
def get_all():
    all_pin = pinOutRepository.all()
    db.session.commit()
    return jsonify(all_pin)

@app.route('/pinout', methods=['POST'])
def insert():
    body = request.get_json(silent=True)
    pinoutModel = None
    if body is None:
        response = ResponseHelper.get_response(400, 'Invalid child')
        return jsonify(response)
    try:
        pinoutModel = PinOutSchema(many=False).load(body, unknown=INCLUDE)
    except ValidationError as error:
        response = ResponseHelper.get_response(400, 'Invalid Pinout Model')
        return jsonify(response)

    db.session.add(pinoutModel)
    db.session.commit()
    return jsonify({'success': True})