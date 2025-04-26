from typing import Dict, List, Tuple, Optional, Any
from app.exception import DatabaseException
from app.models import Film
from app.repositories.film_repo import FilmRepository
from app.schemas.film_schema import films_schema, film_schema


class FilmService:
    @staticmethod
    def get_all_film(filter: Optional[Dict[str, Any]] = None, page: int = 1, per_page: int = 10):
        status, msg, detail = 0, '', None
        try:
            films = FilmRepository.get_list_films(filter)
            status = 1
            msg = "Oke"
            detail = films_schema.dump(films)
        except Exception as err:
            raise DatabaseException()

        return {
            "status": status,
            "msg": msg,
            "detail": {
                "list_film": detail
            }
        }

    @staticmethod
    def get_film_by_id(film_id: int):
        status, msg, detail = 0, '', None
        try:
            film: Film = FilmRepository.get_film_by_id(film_id)
            status = 1
            msg = "Oke"
            detail = film_schema.dump(film)
        except Exception as err:
            raise DatabaseException()

        return {
            "status": status,
            "msg": msg,
            "detail": detail
        }

    @staticmethod
    def create_film(film: Dict[str, Any]):
        status, msg, detail = 0, '', None
        try:
            FilmRepository.create_film(film)
        except Exception as err:
            raise DatabaseException()
        status = 1
        msg = "Oke"
        return {
            "status": status,
            "msg": msg,
            "detail": None
        }
