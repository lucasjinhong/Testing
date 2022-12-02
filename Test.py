import paramiko
import argparse
import os

def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--generate_report',
                    choices=['latest', 'last', 'none'],
                    help='Generate an HTML test report')
    parser.add_argument('Testbed_ID', 
                        help='List the Tesbed_ID to run the tests')
    parser.add_argument('Tests', nargs='*',
                        help='List of test/campaigns to run')
    return parser.parse_args()

def get_testbed_ip(id):
    try:
        ip_addr = '10.29.51.83'
        # ip_addr = subprocess.check_output(['./bed.sh', '-b', id])
        # ip_addr = ip_addr.decode('ascii').split('\t')[1]
    except:
        raise ValueError('Testbed_ID not found')

    return ip_addr

def get_test_report(ip_addr, time, remote_path, version_name):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    print(ip_addr)
    ssh_client.connect(ip_addr, username='vagrant', password='vagrant')

    ftp_client=ssh_client.open_sftp()

    dir_name = remote_path.split('/')[0]
    remote_path = '/home/vagrant/WorkDir/integration/' + remote_path
    local_path = '/home/lkoh/TestBed_Control/bed-control/Testing/'

    # check if local directory exits
    try:
        os.mkdir(local_path)        # Create Testing directory
    except:
        pass

    try:
        local_path = local_path + version_name + '/'
        os.mkdir(local_path)        # Create version directory
    except:
        pass

    try:
        local_path = local_path + time  + '/'
        os.mkdir(local_path)        # Create Time directory
    except:
        pass
    
    # Create Log or Report files directory
    local_path = local_path + dir_name + '/'
    os.mkdir(local_path)

    remote_files = ftp_client.listdir(remote_path)
    print('remote: ', remote_path, '\nlocal : ', local_path)

    # move file from remote to local
    for file in remote_files:
        remote_file_path = remote_path + file
        local_file_path = local_path + file
        ftp_client.get(remote_file_path,local_file_path)
    ftp_client.close()
    ssh_client.close()
    
    # for upload file to jasmine2
    local_path = '/'.join(local_path.split('/')[:-1]) + '/'

    return local_path

def main():
    args = get_args()
    cmd_ssh = '1wqe'
    testbed_ip = get_testbed_ip('qwr')
    cmd_ssh = cmd_ssh + testbed_ip
    get_test_report(testbed_ip, '1', '1', '1')

if __name__ == '__main__':
    main()