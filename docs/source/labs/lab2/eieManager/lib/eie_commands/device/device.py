from abc import ABC, abstractmethod

from numpy import dtype
from ..command import Command

class Device(ABC):
    '''
    Device representation 

    :param str identificator: Identificador number device
    :param str name: Name of the sensor
    :param str dtype: Type of the device
    :param list commands_s: List of commands device supported
    :param str host: IP and host of device 
    '''

    def __init__(
        self, 
        name: str, 
        dtype: str, 
        commands_s: list, 
        host: str) -> None:
        
        self._name = name
        self._dtype = dtype
        self._host = host
        self._commands_s = commands_s



    def name(self) -> str:
        '''
        Gets the name of the device
        '''
        return self._name

    def type(self) -> str:
        """
        Gets the type of device
        """
        return self._dtype


    def commands_supported(self) -> list:
        '''
        Gets the list of commands supported by device
        '''

        return self._commands_s

    def host(self) -> str:
        '''
        Gets the ip and host of device
        '''
        return self._host

    @abstractmethod 
    def read(self) -> float:
        '''
        Reads the device an return it read
        '''
        pass

class DeviceReadCommand(Command):
    """
    Command to read a Device.
    :param device: Device object.
    :type device :class:`Device`
    """
    def __init__(self,device: Device) -> None:
        self.device = device
    def execute(self) -> None:
        """
        Reads the device.
        """
        name = self.device.name()
        dtype = self.device.type()
        commands_s = self.device.commands_supported()
        ip_host = self.device.host()
        print(f"DeviceReadCommand: [{dtype}] {name}: {ip_host}")
        print(f"Commands supported: {commands_s}")