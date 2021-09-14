from flask import Blueprint, jsonify, request, current_app
from repository import PinOutRepository
from common.database import db
from helpers import ResponseHelper
from time import time
from models import PinOut, PinOutSchema
from marshmallow import ValidationError

app = Blueprint('pinout', __name__)
pinOutRepository = PinOutRepository(db)

@app.route('/pinout', methods=['GET'])
def get_all():
    t0 = time()
    all_pin = pinOutRepository.all()
    db.session.commit()
    current_app.logger.info('Get All PinOut Id Total Time: ' + str(time() - t0) + ' seconds')
    return jsonify(all_pin)

@app.route('/pinout', methods=['POST'])
def insert():
    body = request.get_json(silent=True)
    pinoutModel = None
    if body is None:
        response = ResponseHelper.get_response(400, 'Invalid child')
        return jsonify(response)
    try:
        pinoutModel = PinOutSchema(many=False).load(body)
    except ValidationError as error:
        response = ResponseHelper.get_response(400, 'Invalid Pinout Model')
        return jsonify(response)

    db.session.add(pinoutModel)
    db.session.commit()
    return jsonify({'success': True})