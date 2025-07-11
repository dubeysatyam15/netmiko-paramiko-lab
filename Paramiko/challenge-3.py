import paramiko
import time
import getpass

# Create a SSH client
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.load_system_host_keys()

# Router details
password = getpass.getpass(prompt='Enter Password: ', stream=None)
router = {'hostname': '10.1.1.10', 'port':22, 'username': 'u1', 'password': password}
ssh_client.connect(**router, allow_agent=False, look_for_keys=False)

shell = ssh_client.invoke_shell()
shell.send('show users\n')
time.sleep(1)

# Save the output to a file
with open('router-users.txt', 'w') as f:
    f.write(shell.recv(10000).decode('utf-8'))

if ssh_client.get_transport().is_active() == True:
    print('Closing connection')
    ssh_client.close()