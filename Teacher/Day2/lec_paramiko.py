import paramiko
from paramiko import SSHClient
from scp import SCPClient
import os
import stat
from icecream import ic
import time

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

    #######################################################################################
    # Execute Shell Command
    #######################################################################################
    def exeCommand(self, command, isReturn=False):
        # stdin, stdout, stderr = self.client.exec_command(command)
        stdin, stdout, _ = self.client.exec_command(command)

        if isReturn is True:
            return stdout.readlines()

    #######################################################################################
    # Execute SUDO Shell Command
    #######################################################################################
    def sudoCommand(self, command, isReturn=False):
        stdin, stdout, stderr = self.client.exec_command('sudo ' + command, get_pty=True)

        time.sleep(5)
        stdin.write(self.password + '\n')
        stdin.flush()

        if isReturn:
            return stdout.readlines()

if __name__ == '__main__':
    ssh = MySSH()
    # elias.kim@lge.com
    try:
        if ssh.connect('139.150.74.115', 'student', 'student', timeout=5, port=22):
            ic('SSH is connected')
        else:
            ic('Connection is failed')
            exit()

        # 현재 프로세스 목록파일 만들기
        # ssh.exeCommand('ps -ef > process_list.txt', False)

        # ls-al 명령어로 파일목록 가져오기
        # filelist = ssh.exeCommand('ls -al', True)
        #
        # for file in filelist:
        #     # print(file, end='')
        #     # print(file[:-1])
        #     ic(file[:-1])

        # Temp 폴더로 이동 후, 파일목록을 가져오기
        # cd temp
        # ls -al

        # 각각 실행 후 터미널이 닫힘
        # ssh.exeCommand('cd temp')
        # for file in ssh.exeCommand('ls -al', True):
        #     ic(file[:-1])

        # ; - 앞의 명령어가 실패해도 다음 명령어를 실행
        # && - 앞의 명령어가 성공했을때 다음 명령어가 실행
        # & - 앞의 명령어는 백그라운드로 실행하고 동시에 뒤의 명령어를 실행
        # for file in ssh.exeCommand('cd temp;ls -al;pwd', True):
        #     ic(file[:-1])

        # 쉘 스크립트 파일 생성 후 실행
        # ssh.exeCommand('echo "ls -al" > filelist.sh')
        # ssh.exeCommand('chmod 777 ./filelist.sh')
        # for file in ssh.exeCommand('./filelist.sh', True):
        #     ic(file[:-1])

        # sudo 실행불가
        # ssh.exeCommand('sudo mkdir /mytemp;student;')
        ssh.sudoCommand('mkdir /mytemp')

    except Exception as e:
        ic('Exception:', e)
