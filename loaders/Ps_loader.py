from PySide6.QtWidgets import QWidget
from UIs.ui_power_supply import Ui_powerSupply


# class Ps(QWidget, Ui_powerSupply):
class Loader(QWidget, Ui_powerSupply):
    def __init__(self):
        super().__init__(parent=None)

        self.setupUi(self)
