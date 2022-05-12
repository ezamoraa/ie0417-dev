import json

path = './config/devices.json'


def readJSON():
    with open(path, 'r') as f:
        devices = json.load(f)['devices']
    return devices
