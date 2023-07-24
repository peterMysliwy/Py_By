from PySide6.QtWidgets import QWidget
from GUI.ui_combo import Ui_combo


class Loader(QWidget, Ui_combo):
    def __init__(self, parent, name, server_gpib):
        super().__init__()

        self.setupUi(self)


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from helpers.gbibSevice import ServerGpib, Message

    app = QApplication()
    server_GPIB = ServerGpib()
    win = Loader(None, '', server_GPIB)
    win.show()
    app.exec()
