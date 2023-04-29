# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'powerSupplyHdosAs.ui'
##
## Created by: Qt User Interface Compiler version 6.3.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QComboBox,
    QDoubleSpinBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        # Form.resize(575, 305)
        # sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        # Form.setSizePolicy(sizePolicy)
        # Form.setMinimumSize(QSize(575, 305))
        # Form.setMaximumSize(QSize(575, 305))
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 570, 300))
        self.widget.setMinimumSize(QSize(500, 300))
        self.widget.setMaximumSize(QSize(600, 300))
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame_6 = QFrame(self.widget)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_4 = QFrame(self.frame_6)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(0, 0))
        self.frame_4.setMaximumSize(QSize(300, 16777215))
        self.frame_4.setFrameShape(QFrame.Box)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_4)
        self.gridLayout.setObjectName(u"gridLayout")
        self.address_lbl = QLabel(self.frame_4)
        self.address_lbl.setObjectName(u"address_lbl")
        font = QFont()
        font.setPointSize(10)
        self.address_lbl.setFont(font)
        self.address_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.address_lbl, 0, 0, 1, 1)

        self.label = QLabel(self.frame_4)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.label, 0, 1, 1, 1)

        self.address_combo = QComboBox(self.frame_4)
        self.address_combo.setObjectName(u"address_combo")

        self.gridLayout.addWidget(self.address_combo, 1, 0, 1, 1)

        self.devName_edit = QLineEdit(self.frame_4)
        self.devName_edit.setObjectName(u"devName_edit")
        self.devName_edit.setFont(font)
        self.devName_edit.setLayoutDirection(Qt.LeftToRight)
        self.devName_edit.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.devName_edit, 1, 1, 1, 1)

        self.current_lbl = QLabel(self.frame_4)
        self.current_lbl.setObjectName(u"current_lbl")
        self.current_lbl.setFont(font)
        self.current_lbl.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.current_lbl, 2, 0, 1, 1)

        self.current_spin = QDoubleSpinBox(self.frame_4)
        self.current_spin.setObjectName(u"current_spin")
        self.current_spin.setFont(font)
        self.current_spin.setLayoutDirection(Qt.LeftToRight)
        self.current_spin.setAlignment(Qt.AlignCenter)
        self.current_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.gridLayout.addWidget(self.current_spin, 2, 1, 1, 1)

        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.Box)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setSpacing(4)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.start_lbl = QLabel(self.frame_3)
        self.start_lbl.setObjectName(u"start_lbl")
        self.start_lbl.setMinimumSize(QSize(50, 22))
        self.start_lbl.setMaximumSize(QSize(70, 22))
        self.start_lbl.setFont(font)

        self.horizontalLayout.addWidget(self.start_lbl)

        self.start_spin = QDoubleSpinBox(self.frame_3)
        self.start_spin.setObjectName(u"start_spin")
        self.start_spin.setMinimumSize(QSize(60, 0))
        self.start_spin.setMaximumSize(QSize(70, 16777215))
        self.start_spin.setSizeIncrement(QSize(0, 0))
        self.start_spin.setFont(font)
        self.start_spin.setAlignment(Qt.AlignCenter)
        self.start_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout.addWidget(self.start_spin)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.stop_lbl = QLabel(self.frame_3)
        self.stop_lbl.setObjectName(u"stop_lbl")
        self.stop_lbl.setMinimumSize(QSize(50, 22))
        self.stop_lbl.setMaximumSize(QSize(70, 22))
        self.stop_lbl.setFont(font)

        self.horizontalLayout_2.addWidget(self.stop_lbl)

        self.stop_spin = QDoubleSpinBox(self.frame_3)
        self.stop_spin.setObjectName(u"stop_spin")
        self.stop_spin.setMinimumSize(QSize(60, 0))
        self.stop_spin.setMaximumSize(QSize(70, 16777215))
        self.stop_spin.setSizeIncrement(QSize(0, 0))
        self.stop_spin.setFont(font)
        self.stop_spin.setAlignment(Qt.AlignCenter)
        self.stop_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_2.addWidget(self.stop_spin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.step_lbl = QLabel(self.frame_3)
        self.step_lbl.setObjectName(u"step_lbl")
        self.step_lbl.setMinimumSize(QSize(50, 22))
        self.step_lbl.setMaximumSize(QSize(70, 22))
        self.step_lbl.setFont(font)

        self.horizontalLayout_3.addWidget(self.step_lbl)

        self.step_spin = QDoubleSpinBox(self.frame_3)
        self.step_spin.setObjectName(u"step_spin")
        self.step_spin.setMinimumSize(QSize(60, 0))
        self.step_spin.setMaximumSize(QSize(70, 16777215))
        self.step_spin.setSizeIncrement(QSize(0, 0))
        self.step_spin.setFont(font)
        self.step_spin.setAlignment(Qt.AlignCenter)
        self.step_spin.setButtonSymbols(QAbstractSpinBox.NoButtons)

        self.horizontalLayout_3.addWidget(self.step_spin)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.gridLayout.addWidget(self.frame_3, 3, 0, 1, 1)

        self.frame = QFrame(self.frame_4)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.listWidget = QListWidget(self.frame)
        __qlistwidgetitem = QListWidgetItem(self.listWidget)
        __qlistwidgetitem.setCheckState(Qt.Checked);
        __qlistwidgetitem1 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem1.setCheckState(Qt.Checked);
        __qlistwidgetitem2 = QListWidgetItem(self.listWidget)
        __qlistwidgetitem2.setCheckState(Qt.Checked);
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setPointSize(9)
        self.listWidget.setFont(font1)
        self.listWidget.setAlternatingRowColors(True)

        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 2)

        self.add_btn = QPushButton(self.frame)
        self.add_btn.setObjectName(u"add_btn")

        self.gridLayout_2.addWidget(self.add_btn, 1, 0, 1, 1)

        self.clearbtn = QPushButton(self.frame)
        self.clearbtn.setObjectName(u"clearbtn")

        self.gridLayout_2.addWidget(self.clearbtn, 1, 1, 1, 1)


        self.gridLayout.addWidget(self.frame, 3, 1, 1, 1)


        self.horizontalLayout_4.addWidget(self.frame_4)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMinimumSize(QSize(240, 0))
        self.frame_5.setMaximumSize(QSize(240, 16777215))
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_5)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setHorizontalSpacing(6)
        self.formLayout.setVerticalSpacing(2)
        self.formLayout.setContentsMargins(-1, -1, 9, -1)
        self.iden_cb = QCheckBox(self.frame_5)
        self.iden_cb.setObjectName(u"iden_cb")
        self.iden_cb.setEnabled(True)
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.iden_cb.sizePolicy().hasHeightForWidth())
        self.iden_cb.setSizePolicy(sizePolicy1)
        self.iden_cb.setMinimumSize(QSize(0, 0))
        self.iden_cb.setMaximumSize(QSize(16777215, 16777215))
        palette = QPalette()
        brush = QBrush(QColor(213, 213, 213, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush)
        brush1 = QBrush(QColor(217, 217, 217, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush1)
        brush2 = QBrush(QColor(227, 227, 227, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush2)
        brush3 = QBrush(QColor(245, 245, 245, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        self.iden_cb.setPalette(palette)
        font2 = QFont()
        font2.setPointSize(10)
        font2.setKerning(True)
        self.iden_cb.setFont(font2)
        self.iden_cb.setLayoutDirection(Qt.LeftToRight)

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.iden_cb)

        self.output_lbl = QLabel(self.frame_5)
        self.output_lbl.setObjectName(u"output_lbl")
        self.output_lbl.setMinimumSize(QSize(100, 0))
        self.output_lbl.setMaximumSize(QSize(100, 16777215))
        self.output_lbl.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.output_lbl)

        self.output_cb = QCheckBox(self.frame_5)
        self.output_cb.setObjectName(u"output_cb")
        self.output_cb.setFont(font)

        self.formLayout.setWidget(4, QFormLayout.FieldRole, self.output_cb)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.formLayout.setItem(2, QFormLayout.LabelRole, self.horizontalSpacer)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.formLayout.setItem(5, QFormLayout.FieldRole, self.verticalSpacer)

        self.tableWidget = QTableWidget(self.frame_5)
        if (self.tableWidget.columnCount() < 2):
            self.tableWidget.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableWidget.rowCount() < 4):
            self.tableWidget.setRowCount(4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setFont(font)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setRowCount(4)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.formLayout.setWidget(6, QFormLayout.SpanningRole, self.tableWidget)


        self.horizontalLayout_4.addWidget(self.frame_5)


        self.verticalLayout_3.addWidget(self.frame_6)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.address_lbl.setText(QCoreApplication.translate("Form", u"device address", None))
        self.label.setText(QCoreApplication.translate("Form", u"measurement name", None))
        self.devName_edit.setPlaceholderText(QCoreApplication.translate("Form", u"enter a name", None))
        self.current_lbl.setText(QCoreApplication.translate("Form", u"current_ma", None))
        self.start_lbl.setText(QCoreApplication.translate("Form", u"start", None))
        self.stop_lbl.setText(QCoreApplication.translate("Form", u"stop", None))
        self.step_lbl.setText(QCoreApplication.translate("Form", u"step", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("Form", u"New Item", None));
        ___qlistwidgetitem1 = self.listWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("Form", u"New Item", None));
        ___qlistwidgetitem2 = self.listWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("Form", u"New Item", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.add_btn.setText(QCoreApplication.translate("Form", u"add", None))
        self.clearbtn.setText(QCoreApplication.translate("Form", u"clear", None))
#if QT_CONFIG(tooltip)
        self.iden_cb.setToolTip(QCoreApplication.translate("Form", u"a visual to find device", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(statustip)
        self.iden_cb.setStatusTip(QCoreApplication.translate("Form", u"a visual to find device", None))
#endif // QT_CONFIG(statustip)
        self.iden_cb.setText(QCoreApplication.translate("Form", u"idenify", None))
        self.output_lbl.setText(QCoreApplication.translate("Form", u"Front", None))
        self.output_cb.setText(QCoreApplication.translate("Form", u"output", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"information", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"results", None));
    # retranslateUi

