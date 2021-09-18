import datetime
from app.extension import db
from app.extension import ma


# Models
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, unique=True, nullable=False)
    first_name = db.Column(db.String(80), nullable=True)
    last_name = db.Column(db.String(80), nullable=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_active = db.Column(db.Boolean, default=True, nullable=False)
    is_verify = db.Column(db.Boolean, default=False, nullable=False)
    created_on = db.Column(db.String(80), nullable=True)
    updated_on = db.Column(db.String(80), nullable=True)
    is_delete = db.Column(db.Boolean, default=False, nullable=True)

    def __repr__(self):
        return 'User : %r' % self.username

# Create schemas for models
class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = User

    id = ma.auto_field()
    firstName = ma.auto_field('first_name')
    lastName = ma.auto_field('last_name')
    username = ma.auto_field('username')
    email = ma.auto_field('email')
    isActive = ma.auto_field('is_active')
    isVerify = ma.auto_field('is_verify')
    updatedOn = ma.auto_field('updated_on')
