import paramiko

def main():
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect('10.29.51.83', username='vagrant', password='vagrant')

    stdin, stdout, stderr = ssh_client.exec_command('ls')

    print(stdout.readlines())

if __name__ == '__main__':
    main()