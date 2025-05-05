from flask import Flask

from app.config import Config
from app.controllers.auth_controller import auth_bp
from app.controllers.city_controller import city_bp
from app.controllers.film_controller import film_bp
from app.error_handler import register_error_handlers
from app.extension import db, ma, jwt, redis_client
from app.repositories.film_repo import FilmRepository


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)
    jwt.init_app(app)
    redis_client.init_app(app)

    # Register Blueprints
    app.register_blueprint(city_bp)
    app.register_blueprint(film_bp)
    app.register_blueprint(auth_bp)

    # Register Error Handlers
    register_error_handlers(app)
    return app
