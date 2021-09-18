import json
from flask import Blueprint, Response, request
from app.common.modules.auth import RequiredAuthToken, GetJwtToken, createUser, loginUser
from app.response import TokenType, StatusType, ResponseModal
from flasgger.utils import swag_from
from app.models import User, UserSchema
# Blueprint for Api App
# This App route url start with '/api'
app = Blueprint('auth', __name__)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Check for null and blank case all data
    if data['email'] is None or data['password'] is None:
        result = ResponseModal(StatusType.fail.value, None, 'Field is empty or null')
        return Response(result, status=400)

    # User login method
    user = loginUser(data)
    if user['canLogin'] is False:
        result = ResponseModal(StatusType.fail.value, None,
                               'User cannot login check your email and password is correct')
        return Response(result, status=401)

    # Get user object by id
    userObj = User.query.filter_by(id=user['data'], is_delete=False).first()

    tokenTime = {"type": TokenType.accessToken.value, "value": 10}
    accessToken = GetJwtToken(userObj, tokenTime)
    tokenTime = {"type": TokenType.refreshToken.value, "value": 1}
    refreshToken = GetJwtToken(userObj, tokenTime)

    tokens = {"accessToken": accessToken, "refreshToken": refreshToken}
    tokens = json.dumps(tokens)
    result = ResponseModal(StatusType.success.value, tokens, 'User login successfully')
    return Response(result, status=200)


@app.route('/refresh-token', methods=['GET'])
@RequiredAuthToken
def refreshToken(current_user):
    userId = current_user.id
    obj = User.query.filter_by(id=userId).first()
    tokenTime = {"type": TokenType.accessToken.value, "value": 10}
    accessToken = GetJwtToken(obj, tokenTime)
    tokens = json.dumps({"accessToken": accessToken})
    result = ResponseModal(StatusType.success.value, tokens, 'User login successfully')
    return Response(result, status=200)
