from dataclasses import dataclass
from Strategy_meas import Meas_strategy
from measurement import Measurement
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


class Server_gpib:
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

    def get_device(self, device_id: str) -> Measurement :
        return self.measurements[device_id]

    def run_strategys(self, actions: List[Message]):
        for msg in actions:
            self.measurements[msg.meas_id].send_message(msg.strategy, msg.data)
