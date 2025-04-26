from typing import Optional, Dict, Any, List

from app.models.film import Film


class FilmRepository:
    @staticmethod
    def get_list_films(filter: Optional[Dict[str, Any]] = None,
                       page: Optional[int] = None,
                       per_page: Optional[int] = None) -> List[Film]:
        query = Film.query
        if filter:
            if filter.get('release_year'):
                query = query.filter(Film.release_year == filter['release_year'])
            if filter.get('rating'):
                query = query.filter(Film.rating == filter['rating'])
            if filter.get('length_from'):
                query = query.filter(Film.length >= filter['length_from'])
            if filter.get('length_to'):
                query = query.filter(Film.length <= filter['length_to'])
            if filter.get('rent_duration'):
                query = query.filter(Film.rental_duration == filter['rent_duration'])

        return query.all()

    @staticmethod
    def get_film_by_id(film_id: int):
        return Film.query.get(film_id)

    @staticmethod
    def get_film_by_title(film_title: str):
        return Film.query.filter_by(title=film_title)

    @staticmethod
    def create_film(film):
        # try:
        #     db.session.begin()
        #     db.session.add(film)
        #     db.session.commit()
        # except Exception as err:
        #     db.session.rollback()
        print("create film success full")
        return
