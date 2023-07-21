from abc import ABC, abstractmethod
from devices.device import Device

class Meas_strategy(ABC):
    @abstractmethod
    def do(self, device: Device, data: dict):
        pass


class change(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.change(data)


class read(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.read()


class setup(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.setup(data)


class state(Meas_strategy):
    def __init__(self, output: bool):
        self.state = output

    def do(self, device: Device, data: dict):
        device.state(self.state)


class Information(Meas_strategy):
    def __init__(self, que):
        self.que = que

    def do(self, device: Device, data: dict):
        device.information(self.que)


class ps_idenify(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.idenify()


class display_msg(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.display_msg(data['text'], data['state'])
