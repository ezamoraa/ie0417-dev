from random import randint

from .devices import Device  # type: ignore


class ConnectedDevice(Device):
    def __init__(self, name: str, ipAddress: str) -> None:
        super().__init__(name, "connected", ipAddress,
                         "Control-cpu-performance")

    def read(self) -> float:
        return randint(1, 50)
