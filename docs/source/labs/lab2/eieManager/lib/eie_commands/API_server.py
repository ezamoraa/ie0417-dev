"""
REST API using FASTAPI for eieManager
"""

from typing import Dict
from unicodedata import name
from fastapi import FastAPI
from pydantic import BaseModel
from .device.manager import DeviceManager


class Device(BaseModel):
    name: str
    type_device: str
    commands_s: list
    host_port: str


app = FastAPI()

device_mgr = DeviceManager("../config/devices_cfg.json")


@app.post("/devices/")
def create_device(device: Device):
    """
    Create a new item and register it

    :param device, new device to register.
    """
    

    new_dict = device_mgr.add_device(device)
    return new_dict


@app.get("/devices/")
def read_devices() -> Dict:
    """
    Get a list of the current items.

    :param int first: First list element to get (optional).
    :param int limit: Maximum number of elements to get (optional).
    """
    return device_mgr.read_devices()


@app.delete("/devices/{device_name}")
def delete_item(device_name: str, status_code=204):
    """
    Unregister and delete item.

    :param str device_name: Name of the device to delete.
    :param int status_code: Default HTTP status code to return.
    """
    dict_delete = device_mgr.delete_device()
    return dict_delete


@app.get("/devices/{device_name}")
def read_item(device_name: str):
    """
    Get specific device from name.

    :param str item_name: Name of the device to get.
    """
    dict_to_read = device_mgr.read_devices
    for dev in dict_to_read["devices"]:
        if dev["names"] == device_name:
            return dev
