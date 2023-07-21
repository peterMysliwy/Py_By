# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'measurementzzGJqH.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_measurement(object):
    def setupUi(self, measurement):
        if not measurement.objectName():
            measurement.setObjectName(u"measurement")
        measurement.resize(1042, 492)
        self.horizontalLayout = QHBoxLayout(measurement)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.frame = QFrame(measurement)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Academy Engraved LET"])
        font.setPointSize(96)
        self.label.setFont(font)

        self.verticalLayout.addWidget(self.label)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(measurement)

        QMetaObject.connectSlotsByName(measurement)
    # setupUi

    def retranslateUi(self, measurement):
        measurement.setWindowTitle(QCoreApplication.translate("measurement", u"Form", None))
        self.label.setText(QCoreApplication.translate("measurement", u"<html><head/><body><p align=\"center\"><span style=\" font-size:96pt;\">graphic goes here</span></p></body></html>", None))
    # retranslateUi

