from common.database import db
from common.marshmallow import ma

from marshmallow import fields, post_load

class PinOut(db.Model):
    __tablename__ = 'pinout'
    id = db.Column(db.Integer, primary_key=True)
    pin_number = db.Column(db.Integer)
    pin_value = db.Column(db.Integer)

class PinOutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = PinOut
        load_instance = True