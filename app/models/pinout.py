import datetime
from app.extension import db
from app.extension import ma


# Models
class PinOut(db.Model):
    __tablename__ = 'pin_out'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    pin_number = db.Column(db.Integer, nullable=True)
    pin_value = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(255), nullable=True)

# Create schemas for models
class PinOutSchema(ma.SQLAlchemySchema):
    class Meta:
        model = PinOut
        load_instance = True

    id = ma.auto_field()
    firstName = ma.auto_field('pin_number')
    lastName = ma.auto_field('pin_value')
    username = ma.auto_field('description')
