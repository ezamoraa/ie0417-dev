from fastapi import FastAPI, Query, HTTPException
from pydantic import BaseModel
from typing import Optional
from fastapi.middleware.cors import CORSMiddleware
import json
from utils import readJSON
from device.deviceManager import DeviceManager

path = '../../config/devices.json'
print(path)
app = FastAPI()
devices = readJSON()

origins = [
        "http://localhost:3000/",
        "localhost:3000"
        ]

app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"]
        )


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


@app.get('/devices')
async def get_all_devices(id: Optional[int] = Query(None,
                          title="Device Id",
                          description="Filter device by id"),
                          name: Optional[str] = Query(None,
                          title="Device name",
                          description="The device name to filter for")):
    device1 = [d for d in devices if d['id'] == id]

    if name is None:
        if id is None:
            return devices
        else:
            return device1
    else:
        device2 = [x for x in devices if name.lower() in x["name"].lower()]

        if id is None:
            return device2
        else:
            combined = [d for d in device1 if d in device2]
            return combined
    return devices


@app.post('/devices', status_code=201)
def add_device(device: Device):
    device_id = max([d['id'] for d in devices]) + 1
    new_device = {
            "id": device_id,
            "name": device.name,
            "commands": device.commands,
            "connectionInfo": device.connectionInfo
            }
    devices.append(new_device)

    with open(path, 'w') as f:
        json.dump(devices, f)
    return new_device


@app.put('/devices', status_code=204)
def update_device(device: Device):
    new_device = {
            "id": device.id,
            "name": device.name,
            "commands": device.commands,
            "connectionInfo": device.connectionInfo
            }
    device_list = [d for d in devices if d["id"] == device.id]
    if len(device_list) > 0:
        devices.remove(device_list[0])
        devices.append(new_device)
        with open(path, 'w') as f:
            json.dump(devices, f)

            return new_device
    else:
        return HTTPException(status_code=404, detail=f"{device.id} not found!")


@app.delete('/devices/{device_id}')
def delete_device(device_id: int):
    device = [d for d in devices if d["id"] == device_id]
    if len(device) > 0:
        device.remove(device[0])
        with open(path, 'w') as f:
            json.dump(devices, f)
    else:
        raise HTTPException(status_code=404, detail=f"There is no {device_id}")


@app.get('/device/{device_command}')
def get_device_commands(device_command: str):
    dev_mngr = DeviceManager(path)
    dtype = dev_mngr.get_devices_types()
    if device_command in dtype:
        name_per_type = dev_mngr.get_device_names_per_type(device_command)
        executed_commands = []
        for i in name_per_type:
            executed_commands.append(dev_mngr.create_device_read_cmd(i))
        return executed_commands
    else:
        raise HTTPException(status_code=404,
                            detail=f"There is no {device_command}")
