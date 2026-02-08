from peewee import Model, CharField, IntegerField
from .database import db


class BaseModel(Model):
    class Meta:
        database = db


class Candle(BaseModel):
    name = CharField()
    candle_type = IntegerField()
