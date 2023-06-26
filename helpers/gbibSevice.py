from dataclasses import dataclass
from helpers.Strategy_meas import Meas_strategy
from helpers.measurement import Measurement
from typing import Dict, List
import string
import random


def generate_id(length: int = 8):
    return "".join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class Message:
    meas_id: str
    strategy: Meas_strategy
    data: {}


class ServerGpib:
    def __init__(self):
        self.measurements: Dict[str, Measurement] = {}

    def connect(self, measurement: Measurement) -> str:
        if measurement.init():
            dev_id = generate_id()
            self.measurements[dev_id] = measurement
            return dev_id
        else:
            return 'Invalid device'

    def close(self, device_id: str):
        self.measurements[device_id].close()
        del self.measurements[device_id]

    def get_device(self, device_id: str) -> Measurement:
        return self.measurements[device_id]

    def get_instrument_list(self) -> list:
        return ['GPIB::001:INSTR', 'GPIB::009:INSTR', 'GPIB::010:INSTR']

    def run_strategy(self, actions: List[Message]):
        for msg in actions:
            self.measurements[msg.meas_id].send_message(msg.strategy, msg.data)
