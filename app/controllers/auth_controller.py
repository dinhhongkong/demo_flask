from flask import Blueprint, jsonify, request
from flask_jwt_extended import create_access_token

from app.exception import WrongParamException
from app.schemas.auth_schema import LoginSchema

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/api/auth/login', methods=['POST'])
def get_all_city():
    try:
        body_data = LoginSchema().load(request.get_json())
    except Exception as err:
        raise WrongParamException()
    claims = {"username": body_data['username'], "role": "admin"}
    access_token = create_access_token(None, additional_claims=claims)
    return jsonify({
        "status": 1,
        "msg": "Oke",
        "details": {
            "username": body_data["username"],
            "token": access_token
        }
    })
