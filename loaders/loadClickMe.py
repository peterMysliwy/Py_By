from PySide6.QtWidgets import QWidget
from UIs.ui_clickMe import Ui_clickMe


# class Clicker(QWidget, Ui_clickMe):
class Loader(QWidget, Ui_clickMe):
    def __init__(self):
        super().__init__(parent=None)

        self.setupUi(self)
