import json
from typing import Optional, List, Dict

from ..command import Command
from .sensors import SensorFactory
from .sensor import Sensor, SensorReadCommand, SensorAnalyzer


class SensorManager:
    """
    Manager class to control sensor objects lifecycle.

    :param str config_filename: Name of the file with the sensors config.
    """
    def __init__(self, config_filename: str) -> None:
        self.config_filename = config_filename
        self.sensor_factory = SensorFactory()
        self.sensors: Dict[str, Sensor] = {}
        self.sensors_per_type: Dict[str, Dict[str, Sensor]] = {}
        self.init_config()

    def _init_sensors_per_type(self):
        """
        Initializes a sensors per-type mapping dictionary.
        """
        for sensor in self.sensors.values():
            stype = sensor.type()
            name = sensor.name()
            if stype not in self.sensors_per_type:
                self.sensors_per_type[stype] = {}
            self.sensors_per_type[stype][name] = sensor

    def init_config(self) -> None:
        """
        Initializes the manager configuration.
        """
        # Parse config file
        with open(self.config_filename) as config_file:
            config_info = json.load(config_file)
            sensors_info = config_info["devices"]
            # Create sensors
            for sensor_info in sensors_info:
                name = sensor_info["name"]
                stype = sensor_info["type"]
                conexion = sensor_info["conexion"]
                self.sensors[name] = self.sensor_factory(name, stype)

        self._init_sensors_per_type()

    def create_new_sensor(self, changes: list):
        self.sensors[changes[0]] = self.sensor_factory(changes[0], changes[1])
        self.sensors_per_type[changes[1]][changes[0]] = self.sensors[changes[0]]

    def update_sensor(self, name: str, changes: list):
        self.sensors[name].update(changes)
    
    def get_sensor_details(self, name: str):
        returnal = [self.sensors[name].name(), self.sensors[name].type(), self.sensors[name].conexion(), self.sensors[name].commands()]
        return returnal

    def delete_sensor(self, name: str):
        stype = self.sensors[name].type()
        self.sensors_per_type[stype].pop(name)
        self.sensors.pop(name)
        #self.sensors_per_type['level'].pop(name)

    def get_sensor_types(self) -> List[str]:
        """
        Returns the list of sensor types.
        """
        return [name for name in self.sensors_per_type.keys()]

    def get_sensor_names(self) -> List[str]:
        """
        Returns the list of sensor names.
        """
        return [name for name in self.sensors.keys()]

    def get_sensor_names_per_type(self, stype: str) -> List[str]:
        """
        Returns the list of sensor names for a sensor type.
        """
        names: List[str] = []
        type_sensors = self.sensors_per_type.get(stype)
        if type_sensors is not None:
            names = [name for name in type_sensors.keys()]
        return names

    def create_sensor_read_cmd(
            self,
            sensor_name: str,
            analyzer: Optional[SensorAnalyzer] = None
    ) -> Command:
        """
        Creates a command to read a sensor.

        :param str sensor_name: Name of the sensor to read.
        :param sensor_name: Name of the sensor to read.
        :param analyzer: Sensor analyzer to send the readings.
        :type analyzer: :class:`SensorAnalyzer`
        """
        sensor = self.sensors[sensor_name]
        return SensorReadCommand(sensor, analyzer)
