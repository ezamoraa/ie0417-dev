"""
Basic REST API client response using requests.
"""

import sys
import requests
import functools
import json.decoder
from pprint import pformat


def print_response(resp):
    try:
        print(pformat(resp.json()), "\n")
    except json.decoder.JSONDecodeError as e:
        print(e)


def getDevice(url):
    res = requests.get(f"{url}/devices")
    print_response(res)
    return res


def main():
    server_url = 'http://127.0.0.1:8000'
    sys_url = sys.argv[1] if (len(sys.argv) >= 2) else None
    url = sys_url or server_url

    wait_enter = functools.partial(input, "Hit Enter ")

    print("Testing GET response from current devices: ")
    wait_enter()
    getDevice(url)

    print("Testing GET response using filters: ")
    wait_enter()
    query = {"id": 1, "name": "pc-lenovo"}
    res = requests.get(f"{url}/devices", params=query)
    print_response(res)

    print("Test POST method adding devices: ")
    wait_enter()
    new_device = {
            "name": "svr-Server",
            "commands": ["connected", "wireless", "coreCPU"],
            "connectionInfo": "127.0.5.1"
            }
    res = requests.post(f"{url}/devices", json=new_device)
    print_response(res)
    getDevice(url)

    print("Testing DELETE method by eliminating a device: ")
    wait_enter()
    res = requests.delete(f"{url}/devices/1")
    print_response(res)


if __name__ == "__main__":
    main()
