import argparse
import json
import logging 
from random import choice

from sympy import arg
from .args import parse_args
from . import command
from .device.manager import DeviceManager

log = logging.getLogger(__name__)

def main():
    """
    Sensor commands application main function.
    """
    args = parse_args()

    config_filename = args.config
    device_type_name = args.device_type
    device_cmd_per_period, device_period_sec = (100, 5)
    alert_cmd_per_period, alert_period_sec = (2, 1)
    num_read_commands = 200

    # Set up command runners
    device_mgr = DeviceManager(config_filename)
    device_cmd_runner = command.CommandRunner(
        cmd_per_period=device_cmd_per_period,
        period_sec=device_period_sec)
    alert_cmd_runner = command.CommandRunner(
        cmd_per_period=alert_cmd_per_period,
        period_sec=alert_period_sec)
    device_cmd_runner.start()
    alert_cmd_runner.start()


    # Generate read commands for temp sensors
    computer_device_names = device_mgr.get_device_names_per_type(device_type_name)
    for _ in range(num_read_commands):
        rand_device_name = choice(computer_device_names)
        read_cmd = device_mgr.create_device_read_cmd(rand_device_name)
        device_cmd_runner.send(read_cmd)

    # Teardown command runners
    device_cmd_runner.stop()
    alert_cmd_runner.stop()


if __name__ == "__main__":
    main()
