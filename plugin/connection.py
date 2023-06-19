import random

from PySide6.QtCore import QObject, Signal


class Shared(QObject):
    signal = Signal(list)


class Gpib_singleton:
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
        return  self.event.signal
