"""
PyZMQ REQ socket client example module.

This is the client script for the zmq_server_rep_pthread program (@ examples/c/zmq_demo).
"""

import time
import zmq
import struct
import json

def config_json(file):
    file_name = open('device_cfg.json')
    payload = json.load(file_name)
    file_name.close()
    payload = json.dumps(payload)
    payload = bytes(payload, 'utf-8')
    return payload

def main():
    commands = ["add", "destroy"]
    payload = config_json('device_cfg.json')
    payload_size = len(payload)

    port = 8888;
    context = zmq.Context()
    print("Connecting to server...")
    client = context.socket(zmq.REQ)
    with client.connect(f"tcp://localhost:{port}"):
        for command in commands:
            command = bytes(command, "utf-8")
            header = struct.pack("< 100s i", command, payload_size)
            print(header, payload)
            client.send(header+payload)

            # Receive response
        ans = client.recv()
        answer, answer_size = struct.unpack('<100s i 100s', ans)
        print(f"Received response [command: {answer}, val_b: {answer_size}]")


if __name__ == "__main__":
    main()
