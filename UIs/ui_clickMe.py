# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clickMeTGnPMD.ui'
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
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_clickMe(object):
    def setupUi(self, clickMe):
        if not clickMe.objectName():
            clickMe.setObjectName(u"clickMe")
        clickMe.resize(630, 475)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(clickMe.sizePolicy().hasHeightForWidth())
        clickMe.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(clickMe)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(clickMe)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.layoutWidget = QWidget(self.frame)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(80, 40, 134, 38))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(15)
        self.label.setFont(font)

        self.horizontalLayout.addWidget(self.label)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setFont(font)

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addWidget(self.frame)


        self.retranslateUi(clickMe)

        QMetaObject.connectSlotsByName(clickMe)
    # setupUi

    def retranslateUi(self, clickMe):
        clickMe.setWindowTitle(QCoreApplication.translate("clickMe", u"Form", None))
        self.label.setText(QCoreApplication.translate("clickMe", u"click", None))
        self.pushButton.setText(QCoreApplication.translate("clickMe", u"click", None))
    # retranslateUi

