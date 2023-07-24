# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'comboEZtUMv.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QWidget)

from plugin.gpib_drop_down import GPIB_drop_down
from plugin.testplugin import TestPlugin

class Ui_combo(object):
    def setupUi(self, combo):
        if not combo.objectName():
            combo.setObjectName(u"combo")
        combo.resize(659, 534)
        self.gridLayout = QGridLayout(combo)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.signalgenerator = GPIB_drop_down(combo)
        self.signalgenerator.setObjectName(u"signalgenerator")

        self.gridLayout.addWidget(self.signalgenerator, 1, 1, 1, 2)

        self.powermeter = GPIB_drop_down(combo)
        self.powermeter.setObjectName(u"powermeter")

        self.gridLayout.addWidget(self.powermeter, 1, 3, 1, 2)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 2, 0, 1, 1)

        self.frequencies_Ghz = TestPlugin(combo)
        self.frequencies_Ghz.setObjectName(u"frequencies_Ghz")

        self.gridLayout.addWidget(self.frequencies_Ghz, 2, 1, 1, 2)

        self.powers_Dbm = TestPlugin(combo)
        self.powers_Dbm.setObjectName(u"powers_Dbm")

        self.gridLayout.addWidget(self.powers_Dbm, 2, 3, 1, 2)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 2, 5, 1, 1)

        self.compression_points = TestPlugin(combo)
        self.compression_points.setObjectName(u"compression_points")

        self.gridLayout.addWidget(self.compression_points, 3, 1, 1, 3)

        self.horizontalSpacer_3 = QSpacerItem(279, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 3, 4, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 4, 2, 1, 1)


        self.retranslateUi(combo)

        QMetaObject.connectSlotsByName(combo)
    # setupUi

    def retranslateUi(self, combo):
        combo.setWindowTitle(QCoreApplication.translate("combo", u"Form", None))
    # retranslateUi

