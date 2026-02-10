
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER
from src.core.paths import IMAGES_PATH


class MainWindow(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, text_align=CENTER, flex=1))
        label = toga.Label("Welcome to Toga again", style=Pack(align_items=CENTER, flex=0.1))
        image = toga.Image(IMAGES_PATH / "reversial" / "hammer.jpg")
        rimage = toga.Image(IMAGES_PATH / "reversial" / "hammer_example.jpg")
        image_view = toga.ImageView(image)
        rimage_view = toga.ImageView(rimage)
        self.add(label)
        self.add(image_view)
        self.add(rimage_view)
