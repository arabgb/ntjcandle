import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER, ROW
from src.core.paths import IMAGES_PATH
from src.services.candle_service import CandleService


class MainWindow(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, text_align=CENTER, flex=1))
        label = toga.Label("Welcome to Toga again",
                           style=Pack(align_items=CENTER, flex=0.1))
        image = toga.Image(IMAGES_PATH / "reversial" / "hammer.jpg")
        rimage = toga.Image(IMAGES_PATH / "reversial" / "hammer_example.jpg")
        image_view = toga.ImageView(image)
        rimage_view = toga.ImageView(rimage)
        self.add(label)
        self.add(image_view)
        self.add(rimage_view)
        service = CandleService()
        candles = service.get_bullish_candles()
        labels = []
        for candle in candles:
            labels.append(toga.Label(candle['name_ar']))

        print(labels)
        box = toga.Box(direction=COLUMN)

        for label in labels:
            box.add(label)

        self.add(box)
