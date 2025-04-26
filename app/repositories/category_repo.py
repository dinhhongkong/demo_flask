from typing import List

from app.models.category import Category


class FilmRepository:
    @staticmethod
    def get_list_category() -> List[Category]:
        return Category.query.all()

    @staticmethod
    def get_category_by_id(category_id: int):
        return Category.query.get(category_id)
