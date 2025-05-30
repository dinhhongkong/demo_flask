from datetime import datetime
from typing import Optional, Dict, Any, List

from app.exception import DatabaseException
from app.models import FilmCategory
from app.models.film import Film
from app.extension import db

from sqlalchemy.orm import joinedload, selectinload
from sqlalchemy.future import select


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
    def create_film(film_data: Dict[str, Any]):
        now = datetime.utcnow().date()
        try:
            film_data['last_update'] = now
            categories = film_data.pop('categories')
            film = Film(**film_data)
            db.session.add(film)
            db.session.flush()
            for category_id in categories:
                film_category = FilmCategory(
                    film_id=film.film_id,
                    category_id=category_id,
                    last_update=now
                )
                db.session.add(film_category)
            db.session.commit()
            return

        except Exception as e:
            db.session.rollback()
            raise DatabaseException()

    @staticmethod
    def get_all_films_with_categories():
        print("da chay get_all_films_with_categories")
        # Truy vấn các phim kèm theo danh mục của chúng
        # films_with_categories = Film.query.options(joinedload(Film.film_category_list).joinedload(FilmCategory.category)).all()
        films_with_categories = Film.query.options(selectinload(Film.film_category_list)
                                                   .selectinload(FilmCategory.category)).all()
        films_data = []
        for film in films_with_categories:
            categories = [film_category.category for film_category in film.film_category_list]  # Lấy tên danh mục của mỗi phim
            films_data.append({
                "film_title": film.title,
                "categories": categories
            })

        return films_data
