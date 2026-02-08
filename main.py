
import toga
from src.gui.main_window import MainWindow
from src.db.init import init_db


class ImgOrg(toga.App):
    def startup(self):
        init_db()
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = MainWindow()
        self.main_window.size = (500, 300)
        self.main_window.show()


def main():
    return ImgOrg(formal_name="nasser image orginization sulotion", app_id="app.be-free.imgorg")


if __name__ == '__main__':
    main().main_loop()
