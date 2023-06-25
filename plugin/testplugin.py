#############################################################################
##
## Copyright (C) 2021 The Qt Company Ltd.
## Contact: http://www.qt.io/licensing/
##
## This file is part of the Qt for Python examples of the Qt Toolkit.
##
## $QT_BEGIN_LICENSE:BSD$
## You may use this file under the terms of the BSD license as follows:
##
## "Redistribution and use in source and binary forms, with or without
## modification, are permitted provided that the following conditions are
## met:
##   * Redistributions of source code must retain the above copyright
##     notice, this list of conditions and the following disclaimer.
##   * Redistributions in binary form must reproduce the above copyright
##     notice, this list of conditions and the following disclaimer in
##     the documentation and/or other materials provided with the
##     distribution.
##   * Neither the name of The Qt Company Ltd nor the names of its
##     contributors may be used to endorse or promote products derived
##     from this software without specific prior written permission.
##
##
## THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
## "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
## LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
## A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
## OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
## SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
## LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
## DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
## THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
## (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
## OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
##
## $QT_END_LICENSE$
##
#############################################################################

from PySide6.QtCore import QSize, Property, Qt
from PySide6.QtWidgets import QWidget, QApplication, QDoubleSpinBox, QLabel, QGridLayout, QPushButton, QHBoxLayout, \
    QListWidget, QVBoxLayout, QAbstractSpinBox, QListWidgetItem


def build_button() -> QDoubleSpinBox:
    button = QDoubleSpinBox()
    button.setMinimumSize(QSize(80, 30))
    button.setAlignment(Qt.AlignmentFlag.AlignCenter)
    button.setButtonSymbols(QAbstractSpinBox.ButtonSymbols.NoButtons)
    button.setMinimum(-100)
    button.setMaximum(100)
    return button


def add_item(name: str, lv: QListWidget):
    item = QListWidgetItem(name, lv)
    item.setCheckState(Qt.CheckState.Checked)
    lv.addItem(item)


class TestPlugin(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._hovered = False

        # build labels and spinBox
        start_lbl = QLabel('Start')
        stop_lbl = QLabel('Stop')
        step_lbl = QLabel('step')
        self.start_btn = build_button()
        self.stop_btn = build_button()
        self.step_btn = build_button()

        # layout for labels and buttons
        button_frame = QGridLayout()
        button_frame.addWidget(start_lbl, 0, 0)
        button_frame.addWidget(stop_lbl, 1, 0)
        button_frame.addWidget(step_lbl, 2, 0)
        button_frame.addWidget(self.start_btn, 0, 1)
        button_frame.addWidget(self.stop_btn, 1, 1)
        button_frame.addWidget(self.step_btn, 2, 1)

        # build push buttons
        self.add_btn = QPushButton('Add')
        self.clear_btn = QPushButton('Clear')
        buttons = QHBoxLayout()
        buttons.addWidget(self.add_btn)
        buttons.addWidget(self.clear_btn)

        self.list_view = QListWidget()
        self.list_lbl = QLabel('some text')
        self.list_lbl.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # layout for buttons abd listview
        user_input = QVBoxLayout()
        user_input.addWidget(self.list_lbl)
        user_input.addWidget(self.list_view)
        user_input.addLayout(buttons, 1)

        # build main layout
        main_layout = QHBoxLayout()
        main_layout.addLayout(button_frame, 0)
        main_layout.addLayout(user_input, 1)
        self.setLayout(main_layout)

        # events for add and clear
        self.add_btn.released.connect(self.build_list)
        self.clear_btn.released.connect(self.clear_list)

        self.objectNameChanged.connect(self.name)

    def build_list(self):
        value = 0
        count = (self.stop_btn.value() - self.start_btn.value()) / self.step_btn.value()
        for a in range(int(count) + 1):
            add_item('{:.2f}'.format(self.start_btn.value() + value), self.list_view)
            value += self.step_btn.value()
        if count % 1:
            add_item('{:.2f}'.format(self.stop_btn.value()), self.list_view)

    def clear_list(self):
        self.list_view.clear()

    def name(self):
        self.list_lbl.setText(self.objectName())

    def setHovered(self, new_hovered):
        self._hovered = new_hovered

    def getHovered(self):
        return self._hovered

    def items(self):
        return [self.list_view.item(index) for index in range(self.list_view.count())]

    def minimumSizeHint(self):
        return QSize(100, 100)

    def sizeHint(self):
        return QSize(300, 200)

    hovered = Property(bool, getHovered, setHovered)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = TestPlugin()
    window.show()
    sys.exit(app.exec())
