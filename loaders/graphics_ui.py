from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QWidget
from GUI.ui_measurement import Ui_measurement
from pathlib import Path


class Loader(QWidget, Ui_measurement):
    def __init__(self, parent, name, server_gpib):
        super().__init__()

        self.setupUi(self)

        picture_name = name + '.bmp'
        picture_path = str(Path().cwd() / 'testsetups' / picture_name)
        picture = QPixmap()
        picture.load(picture_path)
        self.label.setPixmap(QPixmap(picture))


