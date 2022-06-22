from random import randint
from .device import Device

class DEVcomputer(Device):
    def __init__(self,name:str) -> None:
        ip_host = "127.0.0.1" + str(randint(0000,9999))
        commads_s = ["View", "Comment"]
        super().__init__(name, "computer", commads_s, ip_host)

    def read(self) -> float:
        return randint(1, 50)