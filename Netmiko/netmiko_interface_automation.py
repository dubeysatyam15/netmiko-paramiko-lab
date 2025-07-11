from netmiko import ConnectHandler

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
prompter = net_connect.find_prompt()
if '>' in prompter:
    net_connect.enable()

interface = input("Enter the interface you want to enable: ")
output = net_connect.send_command('sh ip interface ' + interface)

if 'Invalid input detected' in output:
    print("Interface " + interface + " does not exist")
else:
    line = output.splitlines()[0]
    if 'down' in line:
        print(f"Interface {interface} is down. Enabling the interface now.")
        net_connect.config_mode()
        print(net_connect.send_command("interface " + interface))
        print(net_connect.send_command("no shutdown"))
        net_connect.exit_config_mode()
        print("#" * 30)
        print("The interface " + interface + " has been enabled.")
    else:
        print(f"Interface {interface} is already enabled.")

print("Disconnecting from the device.")
net_connect.disconnect()