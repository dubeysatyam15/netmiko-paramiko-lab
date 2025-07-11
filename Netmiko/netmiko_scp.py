from netmiko import ConnectHandler
from netmiko import file_transfer

cisco_router = {
    "device_type": "cisco_ios",
    "ip": "192.168.45.10",
    "username": "admin",
    "password": "cisco",
    "port": 22,
    "verbose": True,
    "secret": "cisco"
}

net_connect = ConnectHandler(**cisco_router)
net_connect.enable()

transfer_output = file_transfer(net_connect, source_file='ospf.txt', dest_file='ospfconfig.txt', file_system='disk0:',
                                direction='put', overwrite_file=True)

print(transfer_output)

net_connect.disconnect()
