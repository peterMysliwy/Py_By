from helpers.measurement import Measurement


class Dispatcher(Measurement):
    def __init__(self, device):
        super().__init__()
        self.device = device

    def init(self) -> bool :
        self.device.connect()
        print(f'{self.device.__class__.__name__} -> Initialized')
        return True

    def close(self):
        print(f'{self.device.__class__.__name__} -> close completed')
        self.device.disconnect()
        self.device = None

    def send_message(self, measurement, data: list):
        measurement.do(self.device, data)


