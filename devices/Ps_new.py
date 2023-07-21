from devices.Ps_vintage import Ps_2400


class Ps_2450(Ps_2400):
    def __init__(self, address: str):
        super().__init__(address)

    def set_idd(self, current: int):
        current = current / 1000
        self.power_supply.write(f':CURR:RANG {current}')
        self.power_supply.write(f':SOUR:VOLT:ILIM {current}')
        print(f'{self.__class__.__name__} -> current set to {current}')

    def idenify(self) -> str:
        return self.power_supply.query('*IDN?')

    def _preset(self):
        self.power_supply.write('*RST')
        self.power_supply.write('*ESE 1;*SRE 32;*CLS;:SOUR:VOLT:READ:BACK ON;:SOUR:CURR:READ:BACK ON;')

    def read(self):
        vdd = float(self.power_supply.query(':READ? "defbuffer1", SOUR'))
        idd = float(self.power_supply.query(':READ? "defbuffer1", READ'))
        return [vdd, idd * 1000]

    def display_msg(self, text: str, state: bool):
        if state:
            cmd = 'DISP:SCR USER;'
        else:
            cmd = 'DISP:SCR HOME;'
        cmd += f':DISP:USER2:TEXT "{text}"'
        self.power_supply.write(cmd)
