from device.deviceManager import DeviceManager
import json

path = '../../config/devices.json'
with open(path, 'r') as f:
    devices = json.load(f)

device_manager = DeviceManager(path)

typeDev = device_manager.get_devices_types()
device_manager.get_device_names_per_type()
