from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from UIs.ui_power_supply import Ui_powerSupply
Signal()

class Loader(QWidget, Ui_powerSupply):
    def __init__(self, parent, name, server_gpib):
        super().__init__()
        self.parent = parent
        self.server = server_gpib
        self.setupUi(self)

        self.comboBox.clear()
        self.comboBox.addItem('')
        self.comboBox.insertSeparator(self.comboBox.count())
        self.comboBox.addItem('Refresh')

        # define events
        self.comboBox.textActivated.connect(self.fill_addresses)
        self.add.clicked.connect(self.generate_list)
        self.clear.pressed.connect(self.items.clear)
        self.lineEdit.editingFinished.connect(self.rename_tree_item)
        self.output.stateChanged.connect(self.source_output)

    def fill_addresses(self, text):
        if text == 'Refresh':
            self.comboBox.clear()
            self.comboBox.addItem('')
            self.comboBox.addItems(self.server.get_instrument_list())
            self.comboBox.insertSeparator(self.comboBox.count())
            self.comboBox.addItem('Refresh')


    def generate_list(self):
        """update the listview with values calculated from start, stop and step"""
        count = int((self.stop.value() - self.start.value()) / self.step.value())
        for a in range(count):
            self.items.addItem(str(round(a * self.step.value() + self.start.value(), 2)))
        self.items.addItem(str(round(self.stop.value(), 2)))

    def information(self, data: list):
        print('result fetched')

    def rename_tree_item(self):
        item = self.parent.treeWidget.currentItem()
        item.setText(0, self.lineEdit.text())

    def source_output(self, state: int):
        if state == 0:
            self.output_lbl.setText('Front')
        else:
            self.output_lbl.setText('Rear')
