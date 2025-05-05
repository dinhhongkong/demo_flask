from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship

from app.extension import db


class Category(db.Model):
    __tablename__ = 'category'

    category_id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(25), nullable=False)
    last_update = Column(Date)
    film_categories = relationship("FilmCategory", back_populates="category", lazy=True)
