from devices.device import rm, Device
import time


class Psg(Device):
    def __init__(self, address: str):
        super().__init__()
        self.signal_gen = rm.open_resource(address)
        self.address = address
        print(f'{self.__class__.__name__} -> is valid')

    def connect(self, preset=True):
        if preset:
            self._preset()
        print(f'{self.__class__.__name__} at {self.address} is connected')

    def disconnect(self):
        self.set_state(False)
        print(f'{self.__class__.__name__} at {self.address} is disconnected')
        self.signal_gen = None

    def _preset(self):
        self.signal_gen.write('*RST')
        time.sleep(2)

    def read(self):
        freq = float(self.signal_gen.query(':FREQ?'))
        pwr = float(self.signal_gen.query(':POW?'))
        return [freq / 1e-9, pwr]

    def set_freq(self, freq: float):
        self.signal_gen.write(F':FREQ {freq * 1e9}')
        print(f'{self.__class__.__name__} -> frequency set to {freq/1000000000} GHz')

    def set_power(self, power: float):
        self.signal_gen.write(f':POW {power}')
        print(f'{self.__class__.__name__} -> power set to {power} dBm')

    def set_state(self, state=False):
        self.signal_gen.write(f':OUTP {state}')
        print(f'{self.__class__.__name__} -> state set to {state}')

    def setup(self, data: dict):
        self.set_freq(data['freq'])
        self.set_power(data['power'])
        self.set_state(data['state'])

    def change(self, data: dict):
        self.set_freq(data['freq'])
        self.set_power(data['power'])

    def state(self, state: bool):
        self.set_state(state)
