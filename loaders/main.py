from PySide6.QtCore import Qt, QVariantAnimation, Slot
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem, QWidget, QMenu
import importlib
from pathlib import Path

from GUI.container import Ui_MainWindow
from helper_class.slide_anim import Slider
from helpers.gbibSevice import ServerGpib
from toolBox.tree_utility import get_subtree_nodes, get_all_items

picture_path = Path.cwd() / 'testsetups'
pictures = [pict.name.removesuffix(".bmp") for pict in picture_path.iterdir() if pict.match('*.bmp')]
MEASUREMENTS = {key: 'loaders.graphics_ui' for key in pictures}


PLUG_IN = {'chart': 'loaders.chart', 'power_supply': 'loaders.power_supply',
           'power_measurement': 'loaders.power_measurement'}


class Experiment(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Experiment, self).__init__()

        self.setupUi(self)
        self.server_GPIB = ServerGpib()

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
        self.actionrun.triggered.connect(self.start)
        self.actionshow.triggered.connect(self.slider.hide_show)
        self.actionstop.triggered.connect(self.stop)

    def _show_context_menu(self, position):
        menu = QMenu()
        current_name = self.treeWidget.currentItem().data(1, 0).objectName()
        if current_name == 'chart':
            self.plugin_name = MEASUREMENTS
            sub_menu = menu.addMenu('Add')
            for key in MEASUREMENTS.keys():
                sub_menu.addAction(key)
        elif current_name == 'measurement':
            self.plugin_name = PLUG_IN
            sub_menu = menu.addMenu('Add')
            for key in PLUG_IN.keys():
                sub_menu.addAction(key)

        menu.triggered.connect(self.menu_item_selected)
        menu.exec(self.treeWidget.mapToGlobal(position))

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
        self.treeWidget.setCurrentItem(item)

    @Slot(str)
    def tree_name_change(self, new_name: str):
        item = self.treeWidget.currentItem()
        item.setText(0, new_name)

    def tree_root(self, widget: QWidget):
        """ This is only used once refactor and move under chart """
        parent = QTreeWidgetItem(self.treeWidget)
        parent.setText(0, widget.objectName())
        parent.setData(1, 0, widget)

    def change_stacked_view(self, current_item: QTreeWidgetItem):
        self.stackedWidget.setCurrentWidget(current_item.data(1, 0))

    def start(self, event: bool):
        # gui change setup for running
        self.tabWidget.setCurrentIndex(0)
        item = self.treeWidget.topLevelItem(0)
        self.change_stacked_view(item)
        self.treeWidget.setCurrentItem(item)
        self.slider.start_changed(event)

        items = get_all_items(self.treeWidget)
        del items[0]  # remove the top item

        measurements = {}
        for item in items:
            """dictionary format KEY = measurement name, VALUES = measurement classes"""
            if item.childCount() > 0:
                children = get_subtree_nodes(item)
                kids = [name.data(1, 0) for name in children]
                del kids[0]  # I don't need the parent
                measurements[item.text(0)] = kids

        print(f'dictionary -> {measurements}')


    def stop(self):
        self.slider.stop_changed()
