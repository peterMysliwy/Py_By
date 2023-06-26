from devicesParent.deviceParent import Device_parent


class PowerSupply(Device_parent):
    def __init__(self, resource):
        super().__init__()
        self.voltage = 0.0
        self.current = 0.0
        self.state = False
        self.inst = resource
        self.channel = 0

    def preset(self):
        self.inst.write('*RST')

    def error_check(self):
        err = self.inst.query_ascii_values("SYST:ERR?", converter='s')
        try:
            err[0] = int(err[0])
        except:
            pass
        return tuple(err)
