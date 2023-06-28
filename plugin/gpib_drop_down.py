#############################################################################
##
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

import random
from PySide6.QtCore import QSize, Slot, Qt, QObject, Signal
from PySide6.QtWidgets import QComboBox, QApplication, QVBoxLayout, QWidget, QMainWindow, QLabel, QHBoxLayout


class Shared(QObject):
    signal = Signal(list)


class GpibSingleton:
    __isinstance = None

    def __new__(cls, *args, **kwargs):
        if cls.__isinstance is None:
            cls.__isinstance = super().__new__(cls)
            cls.event = Shared()
            cls._address_list = []
        return cls.__isinstance

    def __init__(self):
        pass

    def _generate_list(self):
        self._address_list = [f'GPIB::00{random.randint(0, 32)}::INSTR' for a in range(5)]
        self._list_sort()

    def _list_sort(self):
        number = [int(value[6:-7]) for value in self._address_list]    # strip out address numbers
        number.sort()
        self._address_list = [f'GPIB::00{a}::INSTR' for a in number]   # rebuild the list

    @property
    def addresses(self) -> list:    # delete
        return self._address_list

    def refresh(self):
        self._generate_list()
        return self._address_list

    @property
    def shared_signal(self):
        return self.event.signal


class GPIB_drop_down(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.gpib_resource = GpibSingleton()

        self.combo_box = QComboBox()
        self.combo_box.setPlaceholderText('select address')
        self.combo_box.setMinimumSize(QSize(160, 20))

        self.label = QLabel('some text')
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        layout = QHBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.combo_box)
        self.setLayout(layout)

        self._populate_drop_down(self.gpib_resource.addresses)  # this should be an empty list

        self.objectNameChanged.connect(self.set_name)
        self.combo_box.textActivated.connect(self.populate_drop_down)
        self.gpib_resource.shared_signal.connect(self._populate_drop_down)

    def minimumSizeHint(self):
        return QSize(250, 40)

    def set_name(self):
        self.label.setText(self.objectName())

    def populate_drop_down(self, selection: str):
        if selection == 'Refresh':
            self.gpib_resource.shared_signal.emit(self.gpib_resource.refresh())

    @Slot(list)
    def _populate_drop_down(self, items: list):
        self.combo_box.clear()
        self.combo_box.addItem('')
        self.combo_box.addItems(items)
        self.combo_box.insertSeparator(len(items) + 1)
        self.combo_box.addItem('Refresh')

    def sizeHint(self):
        return QSize(300, 40)


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)

    window = QMainWindow()
    drop1 = GPIB_drop_down()
    drop2 = GPIB_drop_down()

    layout = QVBoxLayout()
    layout.addWidget(drop1)
    layout.addWidget(drop2)

    widget = QWidget()
    widget.setLayout(layout)

    window.setCentralWidget(widget)
    window.show()
    sys.exit(app.exec())
