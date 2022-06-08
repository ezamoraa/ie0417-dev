from abc import ABC, abstractmethod

from .commands.command import Command  # type: ignore


class Device(ABC):
    """
    Generic device representation.

    :param str name: Name of the device.
    :param str dtype: Type of the device.
    :param str ipAddress: IP Address of the device.
    """
    def __init__(self, name: str, dtype: str, ipAddress: str,
                 executedCommand: str) -> None:
        self._name = name
        self._type = dtype
        self._address = ipAddress
        self._executedCommand = executedCommand

    def name(self) -> str:
        """
        Gets the name of the device.
        """
        return self._name

    def type(self) -> str:
        """
        Gets the type of the device.
        """
        return self._type

    def connectionInfo(self) -> str:
        """
        Gets the ip address of the device.
        """
        return self._address

    @abstractmethod
    def read(self) -> float:
        """
        Reads the device.
        :return: Device reading.
        """
        pass


class DeviceAnalyzer(ABC):
    """
    Generic and basic device analyzer that processes updates from device reads.
    """
    @abstractmethod
    def update(self, value: float):
        """
        Updates the analyzer state with a new device reading.

        :param float value: Device reading value.
        """
        pass


class DeviceReadCommand(Command):
    """
    Command to read a Device.

    :param device: Device object.
    :type device :class:`Device`
    """
    def __init__(self, device: Device) -> None:
        self.device = device

    def execute(self) -> None:
        """
        Reads the device.
        """
        name = self.device.name()
        dtype = self.device.type()
        ipAddress = self.device.connectionInfo()
        value = self.device.read()
        print(f"DeviceReadCommand: [{dtype}] {name}: {value} {ipAddress}")
