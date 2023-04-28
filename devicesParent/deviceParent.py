from abc import ABC



class Device_parent(ABC):
    def __init__(self):
        pass

    def initialize(self):
        pass

    def setup(self):
        pass

    def change(self):
        pass

    def read(self) -> list:
        pass

    def close(self):
        pass