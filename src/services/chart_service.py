from src.db.models import Candle


def create_candle(name: str, candle_type: int):
    return Candle.create(name=name, candle_type=candle_type)


def list_candles():
    return list(Candle.select())
