from PySide6 import QtGui
from PySide6.QtCore import Qt, QEvent, Slot
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QWidget, QMenu, QTreeWidget
import importlib
from experimental.container import Ui_MainWindow

PLUG_IN = {'chart': 'base_uis.UI_chart', 'power supply': 'loaders.Ps_loader', 'clicker': 'loaders.loadClickMe'}


class Experiment(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Experiment, self).__init__()

        self.setupUi(self)
        self.treeWidget.installEventFilter(self)

        chart = self.launch_view('chart')
        self.stackedWidget.addWidget(chart)
        self.tree_root(chart)
        self.treeWidget.topLevelItem(0).text(0)

        # events
        self.treeWidget.itemClicked.connect(self.change_stacked_view)

    def eventFilter(self, source: QTreeWidget, event: QEvent) -> bool:
        if event.type() == QEvent.ContextMenu and source is self.treeWidget:
            menu = QMenu()
            for key in PLUG_IN.keys():
                menu.addAction(key)

            item = menu.exec_(QtGui.QCursor.pos())
            if item is not None:
                process = self.launch_view(item.text())
                self.stackedWidget.addWidget(process)
                self.tree_append(self.treeWidget.currentItem().text(0), process)
                return True
        return super().eventFilter(source, event)

    def launch_view(self, name: str):
        process = importlib.import_module(PLUG_IN[name], '.')
        return process.Loader(self)

    def tree_append(self, parent: str, child_widget: QWidget):
        """
            parent item is the selected item. add item to the last position
            add the child which is the new plug in to column 1
        """
        loc_parent = self.treeWidget.findItems(parent, Qt.MatchFlag.MatchCaseSensitive, 0)
        item = QTreeWidgetItem(loc_parent[0])
        item.setCheckState(0, Qt.Checked)
        item.setText(0, child_widget.objectName())
        item.setData(1, 0, child_widget)

    def tree_root(self, widget: QWidget):
        """
            ##########################################################
            This is only used once refactor and move under chart
            ##########################################################
        """
        parent = QTreeWidgetItem(self.treeWidget)
        parent.setText(0, widget.objectName())
        parent.setData(1, 0, widget)

    def change_stacked_view(self, currentItem: QTreeWidgetItem):
        """
            ################################################################################
            change the selected item and tell the stacked widget to display
            ################################################################################
        """
        items = self.treeWidget.findItems(currentItem.text(0), Qt.MatchFlag.MatchRecursive, 0)
        data = items[0].data(1, 0)
        if data is not None:
            self.stackedWidget.setCurrentWidget(data)
