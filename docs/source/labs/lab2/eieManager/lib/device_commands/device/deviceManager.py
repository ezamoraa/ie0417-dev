import json
from typing import List, Dict

from .commands.command import Command  # type: ignore
from .deviceFactory import DeviceFactory  # type: ignore
from .devices import Device, DeviceReadCommand  # type: ignore


class DeviceManager:
    """
    Device manager that controls device objects.
    :param str json_file: Name of the file with the devices config.
    """
    def __init__(self, json_file: str) -> None:
        self.json_file = json_file
        self.device_factory = DeviceFactory()
        self.devices: Dict[str, Device] = {}
        self.devices_per_type: Dict[str, Dict[str, Device]] = {}
        self.init_config()

    def _init_devices_per_type(self):
        """
        Initializes a device per type dictionary
        """
        for device in self.devices.values():
            dtype = device.type()
            name = device.name()
            if dtype not in self.devices_per_type:
                self.devices_per_type[dtype] = {}
            self.devices_per_type[dtype][name] = device

    def init_config(self) -> None:
        """
        Initializes the manager configuration.
        """
        # Read the config file
        with open(self.json_file) as json_file:
            config_info = json.load(json_file)
            devices_info = config_info

            # Create devices
            for device_info in devices_info:
                for device_type in device_info["commands"]:
                    if device_type == "connected":
                        name = device_info["name"]
                        dtype = device_type
                        ipAddress = device_info["connectionInfo"]
                        self.devices[name] = self.device_factory(name,
                                                                 dtype,
                                                                 ipAddress)
                    else:
                        if device_type == "wifiEnabled":
                            name = device_info["name"]
                            dtype = device_type
                            ipAddress = device_info["connectionInfo"]
                            self.devices[name] = self.device_factory(name,
                                                                     dtype,
                                                                     ipAddress)
        self._init_devices_per_type()

    def get_devices_types(self) -> List[str]:
        """
        Returns the list of the devices types.
        """
        return [type for type in self.devices_per_type.keys()]

    def get_device_names(self) -> List[str]:
        """
        Returns the list of the devices names.
        """
        return [name for name in self.devices.keys()]

    def get_device_names_per_type(self, dtype: str) -> List[str]:
        """
        Returns the list of devices names for a device type.
        """
        names: List[str] = []
        type_devices = self.devices_per_type.get(dtype)
        if type_devices is not None:
            names = [name for name in type_devices.keys()]
        return names

    def create_device_read_cmd(
        self,
        device_name: str
    ) -> Command:
        """
        Creates a command to read a device.

        :param str device_name: Name of the device to read.
        :param device_name: Name of the device to read.
        :param analyzer: Device analyzer to send the readings.
        :type analyzer: :class:`DeviceAnalyzer`
        """
        device = self.devices[device_name]
        return DeviceReadCommand(device)
