from marshmallow import fields

from app.extension import ma


class LoginSchema(ma.SQLAlchemyAutoSchema):
    username = fields.String(required=True)
    password = fields.String(required=True)