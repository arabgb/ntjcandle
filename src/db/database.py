from peewee import SqliteDatabase
from pathlib import Path

DB_PATH = Path.home() / '.ntjcandle' / 'candle.db'
DB_PATH.parent.mkdir(exist_ok=True)

db = SqliteDatabase(DB_PATH)
