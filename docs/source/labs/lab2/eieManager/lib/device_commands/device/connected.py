from random import randint

from .devices import Device

class ConnectedDevice(Device):
    def __init__(self, name: str) -> None:
        super().__init__(name, "connected", "Host")
    
    def read(self) -> float:
        return randint(1, 50)
