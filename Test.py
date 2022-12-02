import paramiko
import argparse

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

def get_test_report(ip_addr):
    ssh_client = paramiko.SSHClient()
    ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh_client.connect(ip_addr, username='vagrant', password='vagrant')

    ftp_client=ssh_client.open_sftp()

def main():
    args = get_args()

    testbed_ip = '10.29.51.83'
    get_test_report(testbed_ip)

if __name__ == '__main__':
    main()