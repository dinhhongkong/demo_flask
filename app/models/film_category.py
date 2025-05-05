from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.extension import db


class FilmCategory(db.Model):
    __tablename__ = 'film_category'

    film_id = Column(Integer, ForeignKey('film.film_id'), primary_key=True)
    category_id = Column(Integer, ForeignKey('category.category_id'), primary_key=True)
    last_update = Column(Date)
    film = relationship("Film", back_populates="film_categories")
    category = relationship("Category", back_populates="film_categories")
