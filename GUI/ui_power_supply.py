# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'power_supplykpOaBi.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
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
from PySide6.QtWidgets import (QAbstractSpinBox, QApplication, QCheckBox, QDoubleSpinBox,
    QFormLayout, QFrame, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

from plugin.gpib_drop_down import GPIB_drop_down
from plugin.testplugin import TestPlugin

class Ui_powerSupply(object):
    def setupUi(self, powerSupply):
        if not powerSupply.objectName():
            powerSupply.setObjectName(u"powerSupply")
        powerSupply.resize(655, 437)
        font = QFont()
        font.setPointSize(14)
        powerSupply.setFont(font)
        self.gridLayout = QGridLayout(powerSupply)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.frame_6 = QFrame(powerSupply)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(570, 380))
        self.frame_6.setMaximumSize(QSize(570, 380))
        self.frame_6.setFrameShape(QFrame.Box)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(2, 2, 2, 2)
        self.frame_2 = QFrame(self.frame_6)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout = QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Power_supply = GPIB_drop_down(self.frame_2)
        self.Power_supply.setObjectName(u"Power_supply")
        font1 = QFont()
        font1.setPointSize(12)
        self.Power_supply.setFont(font1)

        self.verticalLayout.addWidget(self.Power_supply)

        self.frame_8 = QFrame(self.frame_2)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_8)
        self.formLayout.setObjectName(u"formLayout")
        self.current_lbl = QLabel(self.frame_8)
        self.current_lbl.setObjectName(u"current_lbl")
        self.current_lbl.setFont(font)
        self.current_lbl.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.current_lbl)

        self.current = QDoubleSpinBox(self.frame_8)
        self.current.setObjectName(u"current")
        self.current.setMinimumSize(QSize(0, 30))
        self.current.setFont(font)
        self.current.setAlignment(Qt.AlignCenter)
        self.current.setButtonSymbols(QAbstractSpinBox.NoButtons)
        self.current.setDecimals(0)
        self.current.setMaximum(1000.000000000000000)
        self.current.setValue(1.000000000000000)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.current)

        self.name_lbl = QLabel(self.frame_8)
        self.name_lbl.setObjectName(u"name_lbl")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.name_lbl)

        self.name = QLineEdit(self.frame_8)
        self.name.setObjectName(u"name")
        self.name.setMinimumSize(QSize(0, 30))
        self.name.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.name)


        self.verticalLayout.addWidget(self.frame_8)

        self.voltages = TestPlugin(self.frame_2)
        self.voltages.setObjectName(u"voltages")
        self.voltages.setFont(font1)

        self.verticalLayout.addWidget(self.voltages)


        self.horizontalLayout_3.addWidget(self.frame_2)

        self.frame_5 = QFrame(self.frame_6)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.Box)
        self.frame_5.setFrameShadow(QFrame.Sunken)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_5)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, 18, -1, 24)
        self.iden_lbl = QLabel(self.frame_4)
        self.iden_lbl.setObjectName(u"iden_lbl")

        self.verticalLayout_3.addWidget(self.iden_lbl)

        self.output_lbl = QLabel(self.frame_4)
        self.output_lbl.setObjectName(u"output_lbl")

        self.verticalLayout_3.addWidget(self.output_lbl)

        self.sense_lbl = QLabel(self.frame_4)
        self.sense_lbl.setObjectName(u"sense_lbl")

        self.verticalLayout_3.addWidget(self.sense_lbl)

        self.label_4 = QLabel(self.frame_4)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout_3.addWidget(self.label_4)


        self.horizontalLayout_2.addWidget(self.frame_4)

        self.frame_3 = QFrame(self.frame_5)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.NoFrame)
        self.frame_3.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_2 = QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(9, 0, -1, 0)
        self.idenify = QCheckBox(self.frame_3)
        self.idenify.setObjectName(u"idenify")
        self.idenify.setFont(font)

        self.verticalLayout_2.addWidget(self.idenify)

        self.output = QCheckBox(self.frame_3)
        self.output.setObjectName(u"output")

        self.verticalLayout_2.addWidget(self.output)

        self.sense = QCheckBox(self.frame_3)
        self.sense.setObjectName(u"sense")

        self.verticalLayout_2.addWidget(self.sense)

        self.compliance = QCheckBox(self.frame_3)
        self.compliance.setObjectName(u"compliance")
        self.compliance.setChecked(True)

        self.verticalLayout_2.addWidget(self.compliance)


        self.horizontalLayout_2.addWidget(self.frame_3)


        self.horizontalLayout_3.addWidget(self.frame_5)


        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 1, 2, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 2, 1, 1, 1)


        self.retranslateUi(powerSupply)

        QMetaObject.connectSlotsByName(powerSupply)
    # setupUi

    def retranslateUi(self, powerSupply):
        powerSupply.setWindowTitle(QCoreApplication.translate("powerSupply", u"Form", None))
        self.current_lbl.setText(QCoreApplication.translate("powerSupply", u"current", None))
        self.current.setSuffix(QCoreApplication.translate("powerSupply", u" ma", None))
        self.name_lbl.setText(QCoreApplication.translate("powerSupply", u"name", None))
        self.name.setInputMask("")
        self.name.setText("")
        self.name.setPlaceholderText(QCoreApplication.translate("powerSupply", u"insert name", None))
        self.iden_lbl.setText(QCoreApplication.translate("powerSupply", u"device", None))
        self.output_lbl.setText(QCoreApplication.translate("powerSupply", u"front", None))
        self.sense_lbl.setText(QCoreApplication.translate("powerSupply", u"2 wire", None))
        self.label_4.setText(QCoreApplication.translate("powerSupply", u"On", None))
        self.idenify.setText(QCoreApplication.translate("powerSupply", u"idenify", None))
        self.output.setText(QCoreApplication.translate("powerSupply", u"output", None))
        self.sense.setText(QCoreApplication.translate("powerSupply", u"Sense", None))
        self.compliance.setText(QCoreApplication.translate("powerSupply", u"Compliance", None))
    # retranslateUi

