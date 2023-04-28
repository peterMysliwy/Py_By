import random

from PySide6.QtCore import Qt, QPropertyAnimation
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QTreeWidgetItem

# from UIs.UI_chart import ChartView
from UIs.ui_powerSupply import Ui_Form
from UIs.ui_main import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):      # , Ui_MainWindow
    def __init__(self):
        super().__init__()

        # self.main_ui = Ui_MainWindow()
        self.setupUi(self)
        self.setWindowTitle('DEVELOPMENT VERSION Control Products')

        self.amim = QPropertyAnimation(self.leftWidget)
        self.amim.setDuration(250)

        # signals
        self.amim.valueChanged.connect(self.change_width)
        self.actionhide_show_tree.triggered.connect(self.hide_changed)
        self.action_start.triggered.connect(self.toggle_start)
        self.action_stop.triggered.connect(self.stop_timer)

        # create the power supply and add to main
        self.power_supply = Ui_Form()
        self.power_supply.setupUi(self)
        self.horizontalLayout.addWidget(self.power_supply.widget)
        # self.chartView = ChartView()
        # self.horizontalLayout.addWidget(self.chartView.chart_view)

    def addTreeItem(self, treeItem: str):
        item = QTreeWidgetItem()
        item.setCheckState(0, Qt.CheckState.Checked)
        item.setText(0, treeItem)
        self.treeWidget.addTopLevelItem(item)

    def change_width(self, value: int):
        self.leftWidget.setFixedWidth(value)

    def hide_changed(self, event: bool):
        """animate the tree view user widget"""
        if event:
            self.lft_widget = self.leftWidget.width()
            self.amim.setStartValue(self.lft_widget)
            self.amim.setEndValue(0)
        else:
            self.amim.setStartValue(0)
            self.amim.setEndValue(self.lft_widget)
        self.amim.start()

    def stop_timer(self):
        # self.chartView.timer.stop()
        if self.action_start.isChecked():
            self.action_start.toggle()  # reset the start button to off
            self.action_start.setEnabled(True)

    def toggle_start(self):
        # self.chartView.timer.start()
        self.action_start.setEnabled(False)
        if self.leftWidget.width() > 0:
            self.actionhide_show_tree.activate(QAction.ActionEvent.Trigger)
