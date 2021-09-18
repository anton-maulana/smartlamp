from flask import Flask
from app.extension import db, migrate, ma, swagger
from app.controllers import *


# All Apps routes are registered here
def create_app(config_file="config.py"):
    # Flask app initialize
    app = Flask(__name__)

    # All configuration are in config file
    app.config.from_pyfile(config_file)

    # Register blueprints
    app.register_blueprint(UserController, url_prefix='/api')
    app.register_blueprint(AuthController, url_prefix='/api')
    app.register_blueprint(PinOutController, url_prefix='/api')
    # Database connection initialize
    db.init_app(app)

    # Database migrate initialize
    migrate.init_app(app, db)

    # Marshmallow initialize
    ma.init_app(app)

    # Swagger initialize
    swagger.init_app(app)

    # Return App for run in run.py file
    return app


if __name__ == "__main__":
    create_app().run(debug=True, host='0.0.0.0', port=5000)
