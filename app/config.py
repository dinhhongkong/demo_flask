from datetime import timedelta
import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    # Database configuration
    DB_HOST = os.getenv('DB_HOST')
    DB_USERNAME = os.getenv('DB_USERNAME')
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    DB_DATABASE = os.getenv('DB_DATABASE')
    DB_PORT = os.getenv('DB_PORT')

    # config db
    SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True

    # config jwt
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(minutes=180)
    JWT_VERIFY_SUB = False

    # config redis
    REDIS_URL = "redis://localhost:6379/0"
