from abc import ABC

class Device(ABC):
    def __init__(self):
        pass

    def connect(self):
        pass

    def disconnect(self):
        pass

    def setup(self, data: dict):
        pass

    def change(self, data: dict):
        pass

    def read(self, data: dict):
        pass

    def state(self, state: bool):
        pass
