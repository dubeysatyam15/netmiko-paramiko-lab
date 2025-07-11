from netmiko import ConnectHandler

router = {
    "device_type": "cisco_ios",
    "host": "10.15.4.20",
    "username": "dubeysam",
    "password": "cisco",
    "port": 22,
    "verbose": True,
    "secret": "cisco"
}

print("Connecting to device...")
net_connect = ConnectHandler(**router)

print("Sending commands from file to device...")
output = net_connect.send_config_from_file("ospf.txt")

print(output)

print("Disconnecting from device...")
net_connect.disconnect()

