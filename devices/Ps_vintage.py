from devices.device import Device, rm


class Ps_2400(Device):
    def __init__(self, address: str):
        super().__init__()
        self.power_supply = rm.open_resource(address)
        # self.address = address
        print(f'{self.__class__.__name__} -> is valid')

    def connect(self, preset=True):
        if preset:
            self._preset()
        print(f'{self.__class__.__name__} is connected')

    def _preset(self):
        self.power_supply.write('*RST')
        self.power_supply.write('*ESE 1;*SRE 32;*CLS')

    def disconnect(self):
        self.set_state(False)
        print(f'{self.__class__.__name__} is disconnected')
        self.power_supply.close()
        self.power_supply = None

    def display_msg(self, text: str, state: bool):
        self.power_supply.write(f'DISP:WIND1:TEXT:STAT {int(state)}')
        self.power_supply.write(f'DISP:WIND1:TEXT:DATA "{text}"')

    def set_idd(self, current: int):
        current = current/1000
        self.power_supply.write(f'SENS:CURR:PROT {current}')
        self.power_supply.write(f':SENS:CURR:RANG {current}')
        print(f'{self.__class__.__name__} -> current set to {current}')

    def set_vdd(self, volts: float):
        self.power_supply.write(f':SOUR:VOLT {volts}')
        print(f'{self.__class__.__name__} -> voltage set to {volts}')

    def set_state(self, state=False):
        self.power_supply.write(f':OUTP:STAT {int(state)}')
        print(f'{self.__class__.__name__} -> state is set to {int(state)}')

    def setup(self, data: dict):
        self.set_idd(data['idd'])
        self.set_vdd(data['vdd'])
        self.set_state(data['state'])

    def change(self, data: dict):
        self.set_vdd(data['vdd'])

    def read(self):
        vdd = float(self.power_supply.query(':SOUR:VOLT?'))
        idd = float(self.power_supply.query(':SOUR:CURR?'))
        return [vdd, idd * 1000]

    def state(self, state: bool):
        self.set_state(state)