from netmiko import ConnectHandler

cisco_router = {
    'device_type': 'cisco_ios',
    'host': '10.15.4.20',
    'username': 'dubeysam',
    'password': 'cisco',
    'port': 22,        # optional, default is 22
    'secret': 'cisco', # this the enable password
    'verbose': True    # optional, default is False
}

# Common lines in both the methods.
net_connect = ConnectHandler(**cisco_router)

print("Entering the enable mode..")
net_connect.enable()

commands = ["int Eth0/1", "ip address 10.15.3.20 255.255.255.0", "exit", "username netmiko privilege 15 password lambda"]
output = net_connect.send_config_set(commands) # Enters the global configs and executes the command, then exits the global confid mode.
print(output)

# Another way:
# input_commands = 'ip ssh version 2;access-list 1 permit any; ip domain-name awsome.comm'
# net_connect.send_config_set(input_commands.split(';'))

print(net_connect.send_command("show ip int brief"))
print(net_connect.send_command("show run | include username"))

net_connect.send_command("write memory")

print('Closing connection')
net_connect.disconnect()