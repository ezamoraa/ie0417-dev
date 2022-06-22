import json
from typing import Optional, List, Dict

from ..command import Command
from .Factory import DeviceFactory
from .device import Device, DeviceReadCommand


class DeviceManager:
    '''
    Manager class control for devices

    :param str config_filename: Name of the file with 
    devices info
    '''
    def __init__(self, config_filename: str) -> None:
        self.config_filename = config_filename
        self.device_factory = DeviceFactory()
        self.devices : Dict[str, Device] = {}
        self.devices_per_type: Dict[str, Dict[str, Device]] = {}
        self.init_config()



    def _init_devices_per_type(self):
        """
        Initializes device per type dict.
        """
        for device in self.devices.values():
            name = device.name()
            dtype = device.type()
  
            if dtype not in self.devices_per_type:
                self.devices_per_type[dtype] = {}
            self.devices_per_type[dtype][name] = device


    def init_config(self) -> Dict:
        '''
        Initializes the devices from config and return
        the dict
        '''
        #Parse config file
        with open(self.config_filename) as config_filename:
            device_info = json.load(config_filename)
            device_info = device_info["devices"]
            # Create devices
            for device_info in device_info:
                name = device_info["name"]
                dtype = device_info["dtype"]
                commands_s = device_info["commands_s"]
                ip_host = device_info["ip_host"]
                self.devices[name] = self.device_factory(name, dtype)
        self._init_devices_per_type()

    def read_devices(self):
        with open(self.config_filename) as config_filename:
            device_info = json.load(config_filename)
            return device_info
        

    def add_device(
        self, 
        name: str,
        dtype: str,
        commands_s: list,
        ip_host: str
    ) -> Dict:
        '''
        Creates a new device and returns it as Dict
        '''
        new_device = {
            "name": name,
            "dtype": dtype,
            "commands_s": commands_s,
            "ip_host": ip_host
        }

        return new_device
    
    def delete_device(self, name:str) -> Dict:
        """
        Delete a device and return the dict. 
        """
        for device in self.devices:
            if device["name"] == name:
                device.clear()

        return self.devices

    def send_command(self, command: str, name: str) -> str:
        '''
        Sends a command to a device and returns answer
        '''
        for device in self.devices:
            if device["name"] == name:
                lista_commands = device["commands_s"]
                if command in lista_commands:
                    return("Command accepted")
                else: 
                    return("Command denied")

    def get_device_types(self) -> List[str]:
        """
        Returns the list of devices types.
        """
        return [name for name in self.devices_per_type.keys()]

    def get_device_names(self) -> List[str]:
        """
        Returns the list of sensor names.
        """
        return [name for name in self.devices.keys()]

    def get_device_names_per_type(self, stype: str) -> List[str]:
        """
        Returns the list of sensor names for a sensor type.
        """
        names: List[str] = []
        type_devices = self.devices_per_type.get(stype)
        if type_devices is not None:
            names = [name for name in type_devices.keys()]
        return names

    def create_device_read_cmd(
            self,
            device_name: str
    ) -> Command:
        """
        Creates a command to read a sensor.

        :param str sensor_name: Name of the sensor to read.
        :param sensor_name: Name of the sensor to read.
        :param analyzer: Sensor analyzer to send the readings.
        """
        device = self.devices[device_name]
        return DeviceReadCommand(device)