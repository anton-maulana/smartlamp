from app.models import User
from .base import BaseRepository

class UserRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.model = User