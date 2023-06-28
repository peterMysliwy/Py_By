import platform
import sys

from PySide6.QtWidgets import QApplication
from loaders.load_main import Experiment

if platform.system() == 'Windows':
    sys.argv += ['-platform', 'windows:darkmode=2']

if __name__ == '__main__':
    app = QApplication(sys.argv)

    if platform.system() == 'Windows':
        app.setStyle('Fusion')

    window = Experiment()
    window.show()
    app.exec()
