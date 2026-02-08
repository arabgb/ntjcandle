
import toga
from toga.style import Pack
from toga.style.pack import COLUMN, CENTER


class MainWindow(toga.Box):
    def __init__(self):
        super().__init__(style=Pack(direction=COLUMN, text_align=CENTER, flex=1))

        label = toga.Label("Welcome to Toga again", style=Pack(align_items=CENTER, flex=0.1))
        self.add(label)
