"""
Basic REST API client example using requests.
"""

import sys
import requests
import functools
import json.decoder
from pprint import pformat


def main():
    default_url = 'http://127.0.0.1:8000'
    sys_url = sys.argv[1] if (len(sys.argv) >= 2) else None
    url = sys_url or default_url

    wait_enter = functools.partial(input, "Hit Enter ")

    def pprint_response(resp):
        try:
            print(pformat(resp.json()), "\n")
        except json.decoder.JSONDecodeError as e:
            print(e)

    print("Get current items (GET basic):")
    wait_enter()
    resp = requests.get(f"{url}/devices/")
    pprint_response(resp)


    print("Create new item (POST):")
    wait_enter()
    new_item = {
        'name': "HP-Pavilon",
        'dtype': "computer",
        'commands_s': ["Read, Sent", "Destroy"],
        'ip_host': "127.0.0.1.5555"
    }
    resp = requests.post(f"{url}/devices/", json=new_item)
    pprint_response(resp)

    print("Get created item (GET with path param):")
    wait_enter()
    resp = requests.get(f"{url}/devices/AsusVivobook")
    pprint_response(resp)


    print("Destroy created item (DELETE with path param):")
    wait_enter()
    resp = requests.delete(f"{url}/devices/AsusVivobook")
    pprint_response(resp)


if __name__ == "__main__":
    main()
