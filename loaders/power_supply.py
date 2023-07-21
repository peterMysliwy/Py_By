from PySide6.QtCore import Slot
from PySide6.QtWidgets import QWidget

from GUI.ui_power_supply import Ui_powerSupply
from helpers.Strategy_meas import display_msg
from helpers.measurements import Dispatcher
from helpers.utility import device_factory
from helpers.gbibSevice import Message


class Loader(QWidget, Ui_powerSupply):
    def __init__(self, parent, name, server_gpib):
        super().__init__()
        self.parent = parent
        self.__name = 'power_supply'    # has to be hard coded to the device type
        self.server = server_gpib
        self.setupUi(self)
        self.ps_id = ''
        self.dispatcher = None
        self.idenify.setEnabled(False)

        # events for checkboxes
        self.name.editingFinished.connect(self.name_changed)
        self.output.stateChanged.connect(self.change_output)
        self.sense.stateChanged.connect(self.change_sense)
        self.compliance.stateChanged.connect(self.change_comp)
        self.idenify.stateChanged.connect(self.display_identify)
        self.Power_supply.combo_box.textActivated.connect(self.display_ps_name)

    def change_output(self, value: int):
        self.output_lbl.setText('rear' if value else 'front')

    def change_sense(self, value: int):
        self.sense_lbl.setText('4 Wire' if value else '2 Wire')

    def change_comp(self, value: int):
        self.label_4.setText('ON' if value else 'OFF')

    @Slot(str)
    def display_ps_name(self, address: str):
        """ check for a valid devise and generate the device"""
        if address != "Refresh":
            ps = device_factory(address, self.__name)
            self.dispatcher = Dispatcher(ps)
            self.ps_id = self.server.connect(self.dispatcher)
            self.idenify.setEnabled(True)

    def display_identify(self, value: int):
        if value == 2:
            msg = Message(self.ps_id, display_msg(), {'text': self.name.text(), 'state': True})
        else:
            msg = Message(self.ps_id, display_msg(), {'text': '', 'state': False})
        self.server.run_strategy([msg])

    def get_size(self) -> int:
        return self.voltages.list_view.count()

    def name_changed(self):
        if self.parent is not None:
            self.parent.tree_name_change(self.name.text())


if __name__ == '__main__':
    from PySide6.QtWidgets import QApplication
    from helpers.gbibSevice import ServerGpib, Message

    app = QApplication()
    server_GPIB = ServerGpib()
    win = Loader(None, '', server_GPIB)
    win.show()
    app.exec()
