from helpers.device import Device


class Vintage_keithley(Device):
    def __init__(self, address: str):
        super().__init__()
        self.address = address
        print(f'{self.__class__.__name__} -> is valid')

    def connect(self):
        print(f'{self.__class__.__name__} at {self.address} is connected')

    def disconnect(self):
        self.set_state(False)
        print(f'{self.__class__.__name__} at {self.address} is disconnected')
        self.address = None

    def set_idd(self, current: int):
        print(f'{self.__class__.__name__} -> current set to {current/1000}')

    def set_vdd(self, volts: float):
        print(f'{self.__class__.__name__} -> voltage set to {volts}')

    def set_state(self, state=False):
        print(f'{self.__class__.__name__} -> state set to {state}')

    def setup(self, data: dict):
        self.set_idd(data['idd'])
        self.set_vdd(data['vdd'])
        self.set_state(data['state'])

    def change(self, data: dict):
        self.set_vdd(data['vdd'])

    def read(self, data: dict):
        pass

    def state(self, state: bool):
        self.set_state(state)



class New_keithley(Vintage_keithley):
    def __init__(self, address: str):
        super().__init__(address)

    def set_idd(self, current: int):
        print(f'{self.__class__.__name__} -> current set to {current/1000}')

    def set_vdd(self, volts: float):
        print(f'{self.__class__.__name__} -> voltage set to {volts}')

    def set_state(self, state=False):
        print(f'{self.__class__.__name__} -> state set to {state}')



class Sig_gen(Device):
    def __init__(self, address: str):
        super().__init__()
        self.address = address
        print(f'{self.__class__.__name__} -> is valid')

    def connect(self):
        print(f'{self.__class__.__name__} at {self.address} is connected')

    def disconnect(self):
        self.set_state(False)
        print(f'{self.__class__.__name__} at {self.address} is disconnected')
        self.address = None

    def set_freq(self, freq: float):
        print(f'{self.__class__.__name__} -> frequency set to {freq/1000000000} GHz')

    def set_power(self, power: float):
        print(f'{self.__class__.__name__} -> power set to {power} dBm')

    def set_state(self, state=False):
        print(f'{self.__class__.__name__} -> state set to {state}')

    def setup(self, data: dict):
        self.set_freq(data['freq'])
        self.set_power(data['power'])
        self.set_state(data['state'])

    def change(self, data: dict):
        self.set_freq(data['freq'])

    def read(self, data: dict):
        pass

    def state(self, state: bool):
        self.set_state(state)
