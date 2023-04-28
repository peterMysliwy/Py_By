from PySide6.QtWidgets import QWidget, QWidgetItem, QTreeWidgetItem
from UIs.ui_power_supply import Ui_powerSupply


# class Ps(QWidget, Ui_powerSupply):
class Loader(QWidget, Ui_powerSupply):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent
        self.setupUi(self)

        # define events
        self.add.clicked.connect(self.generate_list)
        self.clear.pressed.connect(self.items.clear)
        self.lineEdit.editingFinished.connect(self.rename_tree_item)

    def generate_list(self):
        """update the listview with values calculated from start, stop and step"""
        count = int((self.stop.value() - self.start.value()) / self.step.value())
        for a in range(count):
            self.items.addItem(str(round(a * self.step.value(), 2)))
        self.items.addItem(str(round(self.stop.value(), 2)))

    def rename_tree_item(self):
        item = self.parent.treeWidget.currentItem()
        item.setText(0, self.lineEdit.text())
