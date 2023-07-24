from enum import Enum, auto
from devices.device import rm, Device


class meas_type(Enum):
    CONTav = auto()
    TRACe = auto()
    TGATe = auto()
    TSLot = auto()


class NRP(Device):
    def __init__(self, address: str):
        super().__init__()
        self.rhode_pm = rm.open_resource(address)
        self.min_freq = 0
        self.max_freq = 0
        self.min_pwr = 0
        self.max_pwr = 0
        print(f'{self.__class__.__name__} -> is valid')

    def connect(self, preset=True):
        if preset:
            self._preset()
        print(f'{self.__class__.__name__} is connected')

    def _preset(self):
        self.rhode_pm.write('*RST')
        self.rhode_pm.write('*ESE 1;*SRE 32;*CLS')

    def disconnect(self):
        print(f'{self.__class__.__name__} is disconnected')
        self.rhode_pm.close()
        self.rhode_pm = None

    def _head_mode(self, head: int, meas_type: Enum):
        """       private
        sets the measurement type"""
        self.rhode_pm.write(f'CALC{head}:TYPE {meas_type.name}')

    def setCwMode(self, head: int):
        self._head_mode(head, meas_type.CONTav)

    def setTgateMode(self, head, gate, start, length):
        self._head_mode(head, meas_type.TGATe)
        self.rhode_pm.write(f'CALC{head}:TGAT{gate}:OFFS {start * 1e-06}')
        self.rhode_pm.write(f'CALC{head}:TGAT{gate}:TIME {length * 1e-06}')

    def setTrigger(self, head: int, source: str, slop: str, count: int):
        self.rhode_pm.write(f'TRIG{head}:SLOP {slop}')
        self.rhode_pm.write(f'TRIG{head}:SOUR {source}')
        self.rhode_pm.write(f'TRIG{head}:COUN {count}')

    def setOffset(self, head: int, offset: float):
        self.rhode_pm.write(f'CALC{head}:CORR:OFFS:MAGN {offset}')

    def setOffsetState(self, head: int, state: bool):
        self.rhode_pm.write(f'CALC{head}:CORR:OFFS:STAT {state.__int__()}')

    def setFrequency(self, head: int, frequency: float):
        self.rhode_pm.write(f'SENS{head}:FREQ {frequency}')

    def setAverages(self, averages: int):
        pass

    def setAverageState(self, state: bool):
        pass

    def zeroSensors(self):
        pass

    def change(self, data: dict):
        pass

    def read(self, data: dict):
        return self.rhode_pm.query(f'MEAS{data["head"]}?')

    def setup(self, data: dict):
        pass

    def read_sensor_info(self, head: int):
        """read head information convert to a dictionary set min, max freq and power"""
        info = self.rhode_pm.query(f'SENS{head}:INF?')
        info = list(info)
        del info[len(info) - 1]
        data = {}
        for item in info:
            key = item.split(':')
            data[key[0]] = key[1]
        self.min_pwr = data['MinPower']
        self.max_pwr = data['MaxPower']
        self.min_freq = data['MinFreq']
        self.max_freq = data['MaxFreq']



