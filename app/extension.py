from flask_jwt_extended import JWTManager
from flask_redis import FlaskRedis
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

db = SQLAlchemy()
ma = Marshmallow()
jwt = JWTManager()
redis_client = FlaskRedis(decode_responses=True)
