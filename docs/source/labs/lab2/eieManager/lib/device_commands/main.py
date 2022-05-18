import logging
from random import choice
from args import parse_args
from device.commands import command
from device.deviceManager import DeviceManager

log = logging.getLogger(__name__)


def main():
    """
    Sensor commands application main function.
    """
    args = parse_args()
    json_file = args.config
    device_type_name = args.device_type
    device_cmd_per_period, sensor_period_sec = (100, 5)
    alert_cmd_per_period, alert_period_sec = (2, 1)
    num_read_commands = 200

    # Set up command runners
    device_mgr = DeviceManager(json_file)
    print(device_mgr)
    device_cmd_runner = command.CommandRunner(
        cmd_per_period=device_cmd_per_period,
        period_sec=sensor_period_sec)
    alert_cmd_runner = command.CommandRunner(
        cmd_per_period=alert_cmd_per_period,
        period_sec=alert_period_sec)
    device_cmd_runner.start()
    alert_cmd_runner.start()

    # Generate read commands for temp sensors
    conn_devices_name = device_mgr.get_device_names_per_type(device_type_name)
    for _ in range(num_read_commands):
        rand_device_name = choice(conn_devices_name)
        read_cmd = device_mgr.create_device_read_cmd(rand_device_name)
        device_cmd_runner.send(read_cmd)

    # Teardown command runners
    device_cmd_runner.stop()
    alert_cmd_runner.stop()


if __name__ == "__main__":
    main()
