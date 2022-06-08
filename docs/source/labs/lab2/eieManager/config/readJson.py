import json

path = 'devices.json'
with open(path, 'r') as f:
    file = json.load(f)
    devices_info = file
connectedDev = []
wifiEnabled = []
for i in file:
    for j in i["commands"]:
        if j == "connected":
            connectedDev.append(i["name"])
        else:
            if j == "wifiEnabled":
                wifiEnabled.append(i["name"])
print("Connected type devices: ", connectedDev)
print("\n")
print("WifiEnabled type devices: ", wifiEnabled)
