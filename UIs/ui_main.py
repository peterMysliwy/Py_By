# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_mainOrfKgi.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QSizePolicy,
    QStatusBar, QTabWidget, QToolBar, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 562)
        self.actionhide_show_tree = QAction(MainWindow)
        self.actionhide_show_tree.setObjectName(u"actionhide_show_tree")
        self.actionhide_show_tree.setCheckable(True)
        icon = QIcon()
        icon.addFile(u":/actions/actions/arrow-left-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        icon.addFile(u":/actions/actions/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.On)
        self.actionhide_show_tree.setIcon(icon)
        self.action_start = QAction(MainWindow)
        self.action_start.setObjectName(u"action_start")
        self.action_start.setCheckable(True)
        icon1 = QIcon()
        icon1.addFile(u":/actions/actions/play-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_start.setIcon(icon1)
        self.action_stop = QAction(MainWindow)
        self.action_stop.setObjectName(u"action_stop")
        icon2 = QIcon()
        icon2.addFile(u":/actions/actions/stop-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.action_stop.setIcon(icon2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(600, 450))
        self.centralwidget.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.leftWidget = QWidget(self.centralwidget)
        self.leftWidget.setObjectName(u"leftWidget")
        self.leftWidget.setMinimumSize(QSize(250, 0))
        self.leftWidget.setMaximumSize(QSize(250, 16777215))
        self.verticalLayout = QVBoxLayout(self.leftWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.tabWidget = QTabWidget(self.leftWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.userInfo = QWidget()
        self.userInfo.setObjectName(u"userInfo")
        self.gridLayout = QGridLayout(self.userInfo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.snCodeEdit = QLineEdit(self.userInfo)
        self.snCodeEdit.setObjectName(u"snCodeEdit")

        self.gridLayout.addWidget(self.snCodeEdit, 2, 1, 1, 1)

        self.dateCodeLabel = QLabel(self.userInfo)
        self.dateCodeLabel.setObjectName(u"dateCodeLabel")
        font = QFont()
        font.setPointSize(10)
        font.setItalic(True)
        font.setKerning(False)
        self.dateCodeLabel.setFont(font)

        self.gridLayout.addWidget(self.dateCodeLabel, 1, 0, 1, 1)

        self.dateCodeEdit = QLineEdit(self.userInfo)
        self.dateCodeEdit.setObjectName(u"dateCodeEdit")

        self.gridLayout.addWidget(self.dateCodeEdit, 1, 1, 1, 1)

        self.pathCodeEdit = QLineEdit(self.userInfo)
        self.pathCodeEdit.setObjectName(u"pathCodeEdit")

        self.gridLayout.addWidget(self.pathCodeEdit, 3, 1, 1, 1)

        self.snLabel = QLabel(self.userInfo)
        self.snLabel.setObjectName(u"snLabel")
        self.snLabel.setFont(font)

        self.gridLayout.addWidget(self.snLabel, 2, 0, 1, 1)

        self.pathLabel = QLabel(self.userInfo)
        self.pathLabel.setObjectName(u"pathLabel")
        self.pathLabel.setFont(font)

        self.gridLayout.addWidget(self.pathLabel, 3, 0, 1, 1)

        self.partEdit = QLineEdit(self.userInfo)
        self.partEdit.setObjectName(u"partEdit")

        self.gridLayout.addWidget(self.partEdit, 0, 1, 1, 1)

        self.commentLabel = QLabel(self.userInfo)
        self.commentLabel.setObjectName(u"commentLabel")
        self.commentLabel.setFont(font)

        self.gridLayout.addWidget(self.commentLabel, 4, 0, 1, 1)

        self.commentCodeEdit = QLineEdit(self.userInfo)
        self.commentCodeEdit.setObjectName(u"commentCodeEdit")

        self.gridLayout.addWidget(self.commentCodeEdit, 4, 1, 1, 1)

        self.partLabel = QLabel(self.userInfo)
        self.partLabel.setObjectName(u"partLabel")
        self.partLabel.setFont(font)

        self.gridLayout.addWidget(self.partLabel, 0, 0, 1, 1)

        self.tabWidget.addTab(self.userInfo, "")
        self.setup = QWidget()
        self.setup.setObjectName(u"setup")
        self.verticalLayout_2 = QVBoxLayout(self.setup)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.treeWidget = QTreeWidget(self.setup)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(0, u"Devices");
        self.treeWidget.setHeaderItem(__qtreewidgetitem)
        self.treeWidget.setObjectName(u"treeWidget")

        self.verticalLayout_2.addWidget(self.treeWidget)

        self.tabWidget.addTab(self.setup, "")

        self.verticalLayout.addWidget(self.tabWidget)


        self.horizontalLayout.addWidget(self.leftWidget)

        self.rightWidget = QWidget(self.centralwidget)
        self.rightWidget.setObjectName(u"rightWidget")

        self.horizontalLayout.addWidget(self.rightWidget, 0, Qt.AlignLeft|Qt.AlignTop)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.toolBar.addAction(self.actionhide_show_tree)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.action_start)
        self.toolBar.addAction(self.action_stop)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionhide_show_tree.setText(QCoreApplication.translate("MainWindow", u"hide_show_tree", None))
#if QT_CONFIG(tooltip)
        self.actionhide_show_tree.setToolTip(QCoreApplication.translate("MainWindow", u"hide or show tree", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.actionhide_show_tree.setStatusTip(QCoreApplication.translate("MainWindow", u"show or hide the start menu", None))
#endif // QT_CONFIG(statustip)
        self.action_start.setText(QCoreApplication.translate("MainWindow", u"action_start", None))
#if QT_CONFIG(tooltip)
        self.action_start.setToolTip(QCoreApplication.translate("MainWindow", u"start the measurement", None))
#endif // QT_CONFIG(tooltip)
        self.action_stop.setText(QCoreApplication.translate("MainWindow", u"action_stop", None))
#if QT_CONFIG(tooltip)
        self.action_stop.setToolTip(QCoreApplication.translate("MainWindow", u"start the measurement", None))
#endif // QT_CONFIG(tooltip)
        self.dateCodeLabel.setText(QCoreApplication.translate("MainWindow", u"date code", None))
        self.snLabel.setText(QCoreApplication.translate("MainWindow", u"serial number", None))
        self.pathLabel.setText(QCoreApplication.translate("MainWindow", u"part Path", None))
        self.commentLabel.setText(QCoreApplication.translate("MainWindow", u"comment", None))
        self.partLabel.setText(QCoreApplication.translate("MainWindow", u"part number", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.userInfo), QCoreApplication.translate("MainWindow", u"userInfo", None))
#if QT_CONFIG(statustip)
        self.treeWidget.setStatusTip(QCoreApplication.translate("MainWindow", u"list of devices to test", None))
#endif // QT_CONFIG(statustip)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.setup), QCoreApplication.translate("MainWindow", u"setup", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

