from models import PinOut
from .base import BaseRepository

class PinOutRepository(BaseRepository):
    def __init__(self, db):
        self.db = db
        self.model = PinOut