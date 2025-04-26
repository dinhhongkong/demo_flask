from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

city_bp = Blueprint('city', __name__)


@city_bp.route('/api/get-all-city', methods=['GET'])
@jwt_required()
def get_all_city():
    return jsonify({
        "status": 1,
        "msg": "Oke",
        "details": {
            "my_name": "Kong"
        }
    })
