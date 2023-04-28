import sys

from PySide6.QtWidgets import QApplication
# from PySide6 import QtSvg, QtXml
# from launchMain import MainWindow
from loaders.load_experiment import Experiment

sys.argv += ['-platform', 'windows:darkmode=2']

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Experiment()
    window.show()
    app.exec()
