import paramiko
from scp import SCPClient

ssh_client = paramiko.SSHClient()
ssh_client.load_system_host_keys()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname='192.168.208.132', port=22, username='dubeysam', password='samdubey', allow_agent=False, look_for_keys=False)

scp = SCPClient(ssh_client.get_transport())

# copy a single file to remote server
scp.put('paramiko_ssh.py', 'remote-file.txt')

# copy a directory to remote server
#scp.put('automamtiondirectory', recursive=True, remote_path='/root')

# downloading a file fromm the remote server
scp.get('/etc/passwd', 'passwd')

scp.close()