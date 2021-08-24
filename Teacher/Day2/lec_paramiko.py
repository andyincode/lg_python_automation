import paramiko
from paramiko import SSHClient
from scp import SCPClient
import os
import stat
from icecream import ic

class MySSH():
    def __init__(self):
        self.ftp_client = None
        self.client = None
        self.scp_client = None

    #######################################################################################
    # Connect Host
    #######################################################################################
    def connect(self, host, user_id, user_password, port=22, timeout=None):
        # 연결된 객체가 없으면
        if self.client is None:
            self.client = SSHClient()
            self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            self.client.connect(hostname=host, port=port, username=user_id,
                                password=user_password, timeout=timeout)

            # 연결에 성공하면
            if self.isAlive():
                self.password = user_password
                return True
            else:
                return False

    #######################################################################################
    # Check Connection
    #######################################################################################
    def isAlive(self):
        if self.client is None:
            return None
        else:
            return self.client.get_transport().is_alive()

if __name__ == '__main__':
    ssh = MySSH()
    # elias.kim@lge.com
    try:
        if ssh.connect('139.150.74.115', 'student', 'student', timeout=5, port=22):
            ic('SSH is connected')
        else:
            ic('Connection is failed')
    except Exception as e:
        ic('Exception:', e)
