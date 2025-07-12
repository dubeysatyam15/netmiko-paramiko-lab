#Method 1

#from netmiko import Netmiko
#net_connect = Netmiko(host='10.15.4.20', port='22', username='u1', password='cisco', device_type='cisco_ios')

# Method 2
from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '10.15.4.20',
    'username': 'u1',
    'password': 'cisco',
    'port': 22,        # optional, default is 22
    'secret': 'cisco', # this the enable password
    'verbose': True    # optional, default is False
}

# Common lines in both the methods.
net_connect = ConnectHandler(**cisco_router)
output = net_connect.send_command('show version')
print(output)

# To enter to global configuration mode (conf t)
if not net_connect.check_config_mode():
    net_connect.config_mode()

net_connect.send_command('username Pihu password 1507')

net_connect.exit_config_mode()

print('Closing connection')
net_connect.disconnect()
