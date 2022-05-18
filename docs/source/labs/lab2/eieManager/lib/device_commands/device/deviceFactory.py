"""
Devices module entry point.
"""
from .devices import Device  # type: ignore

from .connected import ConnectedDevice  # type: ignore
from .wifiEnabled import WifiEnabledDevice  # type: ignore


class DeviceFactory():
    """
    Factory that creates a device of a given type name
    """
    def __init__(self) -> None:
        self._device_type_to_cls = {
            "connected": ConnectedDevice,
            "wifiEnabled": WifiEnabledDevice,
        }

    @property
    def supported_types(self):
        """
        Returns the list of names for the supported device types.
        """
        return [dtype for dtype in self._device_type_to_cls.keys()]

    def __call__(self, name: str, dtype: str, ipAddress: str) -> Device:
        """
        Creates the device.

        :param str name: Name of the device to create.
        :param str dtype: Device type.
        """
        device_cls = self._device_type_to_cls[dtype]
        return device_cls(name, ipAddress)
