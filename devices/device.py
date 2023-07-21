from abc import ABC
import pyvisa as visa

rm = visa.ResourceManager()


class Device(ABC):
    def __init__(self):
        ...

    def connect(self):
        ...

    def disconnect(self):
        ...

    def setup(self, data: dict):
        ...

    def change(self, data: dict):
        ...

    def read(self):
        ...

    def state(self, state: bool):
        ...

    def information(self, que):
        ...

    def idenify(self) -> str:
        ...

    def display_msg(self, text: str, state: bool):
        ...