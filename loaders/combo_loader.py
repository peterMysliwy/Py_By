from PySide6.QtWidgets import QWidget
from UIs.ui_combo import Ui_combo


class Loader(QWidget, Ui_combo):
    def __init__(self, parent, name, server_gpib):
        super().__init__()

        self.setupUi(self)