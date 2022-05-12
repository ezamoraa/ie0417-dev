from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional
import json
from setup import readJSON

path = './config/devices.json'
app = FastAPI()
devices = readJSON()
class Device(BaseModel):
    id: Optional[int] = None
    name: str
    commands: list = []
    connectionInfo: str

@app.get('/devices/{device_id}', status_code=200)
def get_devices(device_id: int):
    device = [d for d in devices if d['id'] == device_id]
    print(device)
    return device[0] if len(device) > 0 else {}
print(get_devices(1))

@app.post('/devices', status_code=201)
def add_device(device: Device):
    device_id=max([d['id'] for d in devices]) + 1
    new_device = {
            "id" : device_id,
            "name" : device.name,
            "commands": device.commands,
            "connectionInfo" : device.connectionInfo
            }
    devices.append(new_device)

    with open(path, 'w') as f:
        json.dump(devices, f)
    return new_device
