from app.models.film import Film
from app.extension import ma
from marshmallow import fields, validate


class FilmSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Film
        load_instance = True
        # fields = ("film_id", "title", "release_year", "rating")


class FilterFilms(ma.SQLAlchemyAutoSchema):
    release_year = fields.Integer(required=False)
    rating = fields.String(required=False)
    length_from = fields.String(required=False)
    length_to = fields.Integer(required=False)
    rent_duration = fields.Integer(required=False)


class CreateFilm(ma.SQLAlchemyAutoSchema):
    title = fields.String(required=True, validate=validate.Length(min=5, max=128))
    description = fields.String(required=True, validate=validate.Length(min=5))
    release_year = fields.Integer(required=True)
    language_id = fields.Integer(required=True)
    original_language_id = fields.Integer(required=False, allow_none=True)
    rental_duration = fields.Integer(required=True)
    rental_rate = fields.Decimal(required=True)
    length = fields.Integer(required=True)
    replacement_cost = fields.Decimal(required=True)
    rating = fields.String(required=True)
    special_features = fields.String(required=True)
    categories = fields.List(fields.Integer(), required=True, validate=validate.Length(min=1))


film_schema = FilmSchema()
films_schema = FilmSchema(many=True)
filter_films_schema = FilterFilms()
create_film_schema = CreateFilm()
