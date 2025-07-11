import paramiko
import time

# Create a SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()

# Router details
router = {'hostname': '10.1.1.10', 'port':22, 'username': 'u1', 'password': 'cisco'}
ssh_client.connect(**router, allow_agent=False, look_for_keys=False)

shell = ssh_client.invoke_shell()
shell.send('show users\n')
time.sleep(1)

output = shell.recv(10000).decode('utf-8')
print(output)

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()