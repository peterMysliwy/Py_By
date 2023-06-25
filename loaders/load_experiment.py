from PySide6.QtCore import Qt, QVariantAnimation, Slot, QEvent
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QWidget, QMenu
import importlib

from experimental.container import Ui_MainWindow
from helper_class.slide_anim import Slider
from helpers.gbibSevice import Server_gpib

MEASUREMENTS = {'classic ip3': 'loaders.measurement_loader', 'cancellation ip3': 'loaders.measurement_loader', 'ultra ip3': 'loaders.measurement_loader'}
PLUG_IN = {'chart': 'base_uis.UI_chart',
           'power supply': 'loaders.Ps_loader',
           'clicker': 'loaders.loadClickMe',
           'powerMeasurement': 'loaders.combo_loader'}


class Experiment(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Experiment, self).__init__()

        self.setupUi(self)
        self.server_GPIB = Server_gpib()

        self.plugin_name = PLUG_IN
        self.slide_anim = QVariantAnimation(self)
        self.slider = Slider(self.actionrun, self.actionshow, self.frame, self.slide_anim)

        self.treeWidget.installEventFilter(self)
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)

        chart = self.plugin_launch('chart')
        self.stackedWidget.addWidget(chart)
        self.tree_root(chart)
        del self.plugin_name['chart']
        self.treeWidget.expandAll()

        # events
        self.treeWidget.customContextMenuRequested.connect(self._show_context_menu)
        self.treeWidget.itemClicked.connect(self.change_stacked_view)
        self.treeWidget.itemSelectionChanged.connect(self.tree_change)
        self.actionrun.triggered.connect(self.start)
        self.actionshow.triggered.connect(self.slider.hide_show)
        self.actionstop.triggered.connect(self.stop)

    def _show_context_menu(self, position):
        menu = QMenu()
        current_name = self.treeWidget.currentItem().data(1, 0).objectName()
        if current_name == 'chart':
            sub_menu = menu.addMenu('Add')
            self.plugin_name = MEASUREMENTS
            for key in MEASUREMENTS.keys():
                sub_menu.addAction(key)
        elif current_name == 'measurement':
            self.plugin_name = PLUG_IN
            sub_menu = menu.addMenu('Add')
            for key in PLUG_IN.keys():
                sub_menu.addAction(key)

        menu.triggered.connect(self.menu_item_selected)
        menu.exec(self.treeWidget.mapToGlobal(position))

    def tree_change(self):
        print(f'tree changed ')

    @Slot(QAction)
    def menu_item_selected(self, action: QAction) -> None:
        if action is not None:
            process = self.plugin_launch(action.text())
            self.stackedWidget.addWidget(process)
            self.tree_append(process, action.text())
            self.treeWidget.expandAll()

    def plugin_launch(self, name: str):
        process = importlib.import_module(self.plugin_name[name], '.')
        return process.Loader(self, name, self.server_GPIB)

    def tree_append(self, child_widget: QWidget, name: str):
        """ add the text & child (which is the new plugin) to column 1 """
        item = QTreeWidgetItem(self.treeWidget.currentItem())
        item.setCheckState(0, Qt.Checked)
        item.setText(0, name)
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
