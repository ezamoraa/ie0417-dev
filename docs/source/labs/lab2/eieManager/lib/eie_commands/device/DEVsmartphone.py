from random import randint
from .device import Device

class DEVsmartphone(Device):
    def __init__(self, name: str) -> None:
        ip_host = "192.0.0.1:" + str(randint(0000,9999))
        commands_s = ["Read", "Print", "Cancel"]
        super().__init__(name, "smartphone", commands_s ,ip_host)

    def read(self) -> float:
        return randint(1,50)