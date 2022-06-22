'''
Devices module entry point
'''

from numpy import dtype
from zmq import device
from .device import Device
from .DEVcomputer import DEVcomputer
from .DEVsmartphone import DEVsmartphone


class DeviceFactory():

    """
    Factory creates the dic with devices description
    """
    def __init__(self) -> None:
        self.devices_type_to_cls = {
            "computer": DEVcomputer,
            "smartphone": DEVsmartphone
        }
    @property
    def supported_types(self):
        """
        Returns the list of names for the supported devices types
        """
        return [dtype for dtype in self.devices_type_to_cls.keys()]

    def __call__(self ,name: str, dtype: str) -> Device:

        """
        Creates the device.
        :param str name: Device name
        :param str dtype: Device type
        """

        device_cls = self.devices_type_to_cls[dtype]   
        return device_cls(name)     