from flask import Blueprint, request
from marshmallow import ValidationError

from app.exception import WrongParamException
from app.repositories.film_repo import FilmRepository
from app.schemas.film_schema import filter_films_schema, create_film_schema
from app.services.film_service import FilmService

film_bp = Blueprint('film', __name__)


@film_bp.route('/api/films', methods=['GET'])
def get_all_films_controller():
    # body = request.get_json()
    filter_data = filter_films_schema.load(request.args)
    result = FilmService.get_all_film(filter_data)
    return result


@film_bp.route('/api/film', methods=['GET'])
def get_film_by_id_controller():
    film_id = request.args.get("film_id", type=int)
    if film_id is None or film_id <= 0:
        raise WrongParamException()
    result = FilmService.get_film_by_id(film_id)
    return result


@film_bp.route('/api/create-film', methods=['POST'])
def create_film_controller():
    try:
        body_data = create_film_schema.load(request.get_json())
    except ValidationError as err:
        print("Error: ", err)
        raise WrongParamException()

    result = FilmService.create_film(body_data)
    return result


@film_bp.route('/api/film_test', methods=['GET'])
def abcs():
    result = FilmRepository.get_all_films_with_categories()
    print("ket qua la: ", result)
    return {
        "msg": "oke"
    }
