from src.services.candle_service import CandleService

serive = CandleService()
revaersal = serive.get_reversal_candles()

print(revaersal)
