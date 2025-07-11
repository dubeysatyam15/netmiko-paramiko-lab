import paramiko
import time
import getpass

ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# ssh_client.connect(hostname='172.15.0.5', port=22, username='cisco', password='cisco', look_for_keys=False, allow_agent=False)
# Another way to connect to the SSH server.
# Advantage of using this is that the dict variable can be re-used in the script.

password = getpass.getpass(prompt='Enter Password: ', stream=None)
router = {'hostname':'172.15.0.5', 'port':'22', 'username':'cisco', 'password':password}
ssh_client.connect(**router, look_for_keys=False, allow_agent=False)


# print(ssh_client.get_transport().is_active())

shell = ssh_client.invoke_shell()
shell.send('terminal length 0\n')
shell.send('show version\n')
shell.send('show ip int brief\n')
time.sleep(1)

print('Closing connection...')
ssh_client.close()
