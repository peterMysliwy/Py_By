from devicesParent.power_supply import PowerSupply

class SimPS(PowerSupply):
    def __init__(self):
        super(SimPS, self).__init__(self)

    def set_voltage(self, voltage:  float):
        self.voltage = voltage

    def set_current(self, current: float):
        self.current = current

    def set_state(self, state: bool):
        self.state = state

    def read_voltage(self) -> float:
        return self.voltage

    def read_current(self) -> float:
        return self.current

    def read(self) -> list:
        return [self.voltage, self.current]
