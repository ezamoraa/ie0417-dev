from random import randint

from .devices import Device  # type: ignore


class WifiEnabledDevice(Device):
    def __init__(self, name: str, ipAddress: str) -> None:
        super().__init__(name, "wifiEnabled", ipAddress,
                         "Connect to VPN Address")

    def read(self) -> float:
        return randint(0, 100)
