import os
from dotenv import load_dotenv

load_dotenv()

# Configuration keys are set here
SECRET_KEY = os.getenv('SECRET_KEY')
SQLALCHEMY_DATABASE_URI = os.getenv('SQLALCHEMY_DATABASE_URI')
SQLALCHEMY_TRACK_MODIFICATIONS = os.environ.get('SQLALCHEMY_TRACK_MODIFICATIONS') == 'True' 

# CELERY_BACKEND = os.environ.get('CELERY_BACKEND')
# CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')

