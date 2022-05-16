from random import randint

from .devices import Device

class WifiEnabledDevice(Device):
    def __init__(self, name:str) -> None:
        super().__init__(name, "wifiEnabled", "Guest")

    def read(self) -> float:
        return randint(0, 100)