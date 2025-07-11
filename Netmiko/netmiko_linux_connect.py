from netmiko import ConnectHandler

linux = {
    "device_type": "linux",
    "host": "192.168.208.131",
    "username": "kali",
    "password": "kali",
    "port": 22,
    "verbose": True,
    "secret": "kali"
}

print("Connecting to device...")
net_connect = ConnectHandler(**linux)

net_connect.enable() # Sudo su
output = net_connect.send_command("apt update && apt install -y apache2")

print(output)

print("Disconnecting from device...")
net_connect.disconnect()

