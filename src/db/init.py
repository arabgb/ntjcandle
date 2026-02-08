from .database import db
from .models import Candle

MODELS = [Candle]


def init_db():
    if db.is_closed():
        db.connect
    db.create_tables(MODELS)
