from PySide6 import QtGui
from PySide6.QtCore import Qt, QEvent, QVariantAnimation
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QWidget, QMenu, QTreeWidget
import importlib
from experimental.container import Ui_MainWindow
from helper_class.slide_anim import Slider

MEASUREMENTS = {'classic ip3': 'to be determined', 'cancellation ip3': 'to be determined', 'ultra ip3': 'to be determined'}
PLUG_IN = {'chart': 'base_uis.UI_chart', 'power supply': 'loaders.Ps_loader', 'clicker': 'loaders.loadClickMe'}


class Experiment(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Experiment, self).__init__()

        self.setupUi(self)
        self.treeWidget.installEventFilter(self)

        self.slide_anim = QVariantAnimation(self)
        self.slider = Slider(self.actionrun, self.actionshow, self.frame, self.slide_anim)

        chart = self.launch_view('chart')
        self.stackedWidget.addWidget(chart)
        self.tree_root(chart)
        del PLUG_IN['chart']
        self.treeWidget.expandAll()

        # events
        self.treeWidget.itemClicked.connect(self.change_stacked_view)
        self.actionrun.triggered.connect(self.start)
        self.actionshow.triggered.connect(self.slider.hide_show)
        self.actionstop.triggered.connect(self.stop)

    def eventFilter(self, source: QTreeWidget, event: QEvent) -> bool:
        if event.type() == QEvent.ContextMenu and source is self.treeWidget:
            menu = QMenu()
            menu.addAction('Measurement')
            sub_menu = menu.addMenu('Add')
            for key in PLUG_IN.keys():
                sub_menu.addAction(key)

            item = menu.exec_(QtGui.QCursor.pos())
            if item is not None:
                process = self.launch_view(item.text())
                self.stackedWidget.addWidget(process)
                self.tree_append(process)
                return True
        return super().eventFilter(source, event)

    def launch_view(self, name: str):
        process = importlib.import_module(PLUG_IN[name], '.')
        return process.Loader(self)

    def tree_append(self, child_widget: QWidget):
        """ add the child which is the new plug in to column 1 """
        item = QTreeWidgetItem(self.treeWidget.currentItem())
        item.setCheckState(0, Qt.Checked)
        item.setText(0, child_widget.objectName())
        item.setData(1, 0, child_widget)

    def tree_root(self, widget: QWidget):
        """ This is only used once refactor and move under chart """
        parent = QTreeWidgetItem(self.treeWidget)
        parent.setText(0, widget.objectName())
        parent.setData(1, 0, widget)

    def change_stacked_view(self, currentItem: QTreeWidgetItem):
        self.stackedWidget.setCurrentWidget(currentItem.data(1, 0))

    def start(self, event: bool):
        self.tabWidget.setCurrentIndex(0)
        item = self.treeWidget.topLevelItem(0)
        self.change_stacked_view(item)
        self.treeWidget.setCurrentItem(item)
        self.slider.start_changed(event)

    def stop(self):
        self.slider.stop_changed()
