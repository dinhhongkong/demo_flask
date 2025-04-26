from app.extension import db
from sqlalchemy import Column, Integer, String, Text, Date, Double, ForeignKey


class FilmCategory(db.Model):
    __tablename__ = 'film_category'

    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.category_id'), primary_key=True)
    last_update = Column(Date)
