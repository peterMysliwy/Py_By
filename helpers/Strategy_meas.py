from abc import ABC, abstractmethod
from helpers.device import Device

class Meas_strategy(ABC):
    @abstractmethod
    def do(self, device: Device, data: dict):
        pass

class change(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.change(data)

class read(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.read(data)

class setup(Meas_strategy):
    def do(self, device: Device, data: dict):
        device.setup(data)

class state(Meas_strategy):
    def __init__(self, output: bool):
        self.state = output

    def do(self, device: Device, data: dict):
        device.state(self.state)
