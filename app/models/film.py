from app.extension import db
from sqlalchemy import Column, String, Text, Date, Double, Integer
from sqlalchemy.orm import relationship


class Film(db.Model):
    __tablename__ = 'film'

    film_id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(128), nullable=False)
    description = Column(Text)
    release_year = Column(Integer)
    language_id = Column(Integer)
    original_language_id = Column(Integer)
    rental_duration = Column(Integer)
    rental_rate = Column(Integer)
    length = Column(Integer)
    replacement_cost = Column(Double)
    rating = Column(String, name='rating')
    special_features = Column(String)
    last_update = Column(Date)

    film_category_list = relationship("FilmCategory", backref="film", lazy=True)

    def __repr__(self):
        return f'<Film {self.film_id}: {self.title}>'
