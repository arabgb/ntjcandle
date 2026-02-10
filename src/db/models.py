from peewee import Model, CharField, IntegerField, TextField
from .database import db


class BaseModel(Model):
    class Meta:
        database = db


class Candle(BaseModel):
    name = CharField()
    candle_type = IntegerField()
    description = TextField()
    image_candle_path = CharField()
    image_example_path = CharField()
