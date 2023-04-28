from abc import ABC, abstractmethod
from UIs.ui_main import Ui_MainWindow


class Ui_strategy(ABC):
    @abstractmethod
    def build(self, handle):
        pass


class Development(Ui_strategy):
    """for launching *.UI files """
    def build(self, handle):
        pass


class Release(Ui_strategy):
    """for launching *.py files """
    def build(self, handle:  Ui_MainWindow):
        # self.handle_ui = Ui_MainWindow()
        self.handle_ui = handle.setupUi(self)    # <class 'launchMain.MainWindow'>
        print(self.handle_ui.__class__)
        # self.handle_ui.setup()
        # self.handle_ui.setWindowTitle('Release version')
        # return self.handle_ui
