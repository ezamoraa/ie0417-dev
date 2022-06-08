"""
PyZMQ REQ socket client that sends header and payload for Command.

It sends the req for transportServer who sends out the information
for CommandManager and performs actions upon a determined command.
"""

import time
import zmq
import struct
import random

def main():
    port = 5555
    context = zmq.Context()
    commands = ['est-Connection', 'raise-perfomance', 'encrpyt'] #establish Connection
    payload_size = 32
    print("Connecting to server")
    client = context.socket(zmq.REQ)
    with client.connect(f"tcp://localhost:{port}"):
        for i in range(10):
            # Send request
            cmd_name = random.choice(commands)
            s = bytes(cmd_name, 'utf-8')
            header = struct.pack('32sI', s, payload_size)
            client.send(header)

            # Receive response
            rep = client.recv()
            rep_buffer, rep_b = struct.unpack('<QB', rep)
            print(f"RECEIVED [buffer: {rep_buffer}, repeated: {rep_b}]")
if __name__ == "__main__":
    main()