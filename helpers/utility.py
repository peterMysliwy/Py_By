import json
from pathlib import Path
import importlib
import logging
import pyvisa as visa

logging.basicConfig(filename='utility_logging.conf', format='%(asctime)s %(message)s', filemode='w', level='ERROR')

path = Path().cwd()
if path.name != 'cpNew':
    current_path = path.parent / 'devices'  # C:\Users\pmysliwy\Desktop\cpNew\devices
else:
    current_path = path / 'devices'  # C:\Users\pmysliwy\Desktop\devices

print(f'current path -> {current_path}')


def get_device(name: list[str], address: str):
    path = 'devices.' + name[0]
    module = importlib.import_module(path, '.')
    new_class = getattr(module, name[1])
    return new_class


def find_device(dev_type: str, idn_name: str) -> list[str]:
    new_path = current_path / 'devices_list.json'
    with open(new_path) as file:
        devices_list = dict(json.load(file))
    try:
        devices = devices_list[dev_type]
        return devices[idn_name]
    except Exception as e:
        logging.error(e)
        return ['Error']


def do_idn(address: str):
    rm = visa.ResourceManager()
    instr = rm.open_resource(address)
    try:
        instr.timeout = 500
        result = instr.query('*IDN?')
        result = result.split(',')
        instr.close()
        return result[1]
    except Exception as e:
        logging.error(e)
        return "Error"


def device_factory(address: str, device_kind: str):
    name = do_idn(address)
    if name != 'Error':
        data = find_device(device_kind, name)
        if data != 'Error':
            device = get_device(data, address)
            instrument = device(address)
            return instrument
        else:
            return data


if __name__ == '__main__':
    address = 'GPIB0::10::INSTR'
    new_device = device_factory(address, 'power_supply')
    if new_device != 'Error':
        new_device.set_idd(20)
        new_device.set_vdd(3.01)
        new_device.set_state(True)
        print(new_device.read())
        new_device.set_state(False)
