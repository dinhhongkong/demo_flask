from flask import Flask

from app.config import Config
from app.controllers.city_controller import city_bp
from app.controllers.film_controller import film_bp
from app.error_handler import register_error_handlers
from app.extension import db,ma


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    ma.init_app(app)

    # Register Blueprints
    app.register_blueprint(city_bp)
    app.register_blueprint(film_bp)

    # Register Error Handlers
    register_error_handlers(app)
    return app
