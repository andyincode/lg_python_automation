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

        stdin.write(self.password + '\n')
        stdin.flush()

        # if isReturn:
        #     return stdout.readlines()

        readed = stdout.readlines()
        if isReturn:
            return readed

    #################################################### SFTP ##########################################################

    #######################################################################################
    # Get File From Host (SFTP)
    # srcFilePath: Server(host), dstFilePath: Local(PC, Client)
    #######################################################################################
    def getFromHost(self, srcFilePath, dstFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()

        self.ftp_client.get(srcFilePath, dstFilePath)

    ######################################################################
    # Put File from Host (SFTP)
    # srcFilePath: Local(PC, client), dstFilePath: Server(host)
    def putToHost(self, srcFilePath, dstFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()
        self.ftp_client.put(srcFilePath, dstFilePath)

    ######################################################################
    # Rename file to host
    # FilePath: Server(host) dstFilePath: Server(host)
    def renameHostFile(self, srcFilePath, dstFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()
        self.ftp_client.rename(srcFilePath, dstFilePath)

    ######################################################################
    # Delete file to host
    # srcFilePath: Server(host)
    def deleteHostFile(self, srcFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()
        self.ftp_client.remove(srcFilePath)

    ######################################################################
    # Get file list of host
    # srcFilePath: Server(host)
    def getFileListFromHost(self, srcFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()
        return self.ftp_client.listdir(srcFilePath)

    ######################################################################
    # Get file list of host
    # srcFilePath: Server(host)
    def getFileAttrListFromHost(self, srcFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()
        return self.ftp_client.listdir_attr(srcFilePath)

    ######################################################################
    # Delete folder of host
    # srcFilePath: Server(host)
    def deleteHostFolder(self, srcFilePath):
        if self.ftp_client is None:
            # Get SFTP object from SSHClient
            self.ftp_client = self.client.open_sftp()

        # # Only current folder only
        # file_list = self.getFileListFromHost(srcFilePath) # ~/temp
        # for file in file_list:
        #     file_path = os.path.join(srcFilePath, file) # ~/temp/a.txt ~/temp/b.txt
        #     file_path = file_path.replace('\\', '/')
        #     self.deleteHostFile(file_path)

        # Delete all subfolder recursive
        file_attr_list = self.ftp_client.listdir_attr(srcFilePath)
        for file_attr in file_attr_list:
            path = os.path.join(srcFilePath, file_attr.filename)
            path = path.replace('\\', '/')
            # Path is Folder type
            if stat.S_ISDIR(file_attr.st_mode):
                self.deleteHostFolder(path)
            # Path is File type
            else:
                self.deleteHostFile(path)

        self.ftp_client.rmdir(srcFilePath)

    ################################################SCP################################################################

    ######################################################################
    # Get file from host with SCP
    # srcFilePath: Server(host) dstFilePath: Local(PC, client)
    def getFromHostWithSCP(self, srcFilePath, dstFilePath):
        if self.scp_client is None:
            self.scp_client = SCPClient(self.client.get_transport())
        self.scp_client.get(srcFilePath, dstFilePath)

    ######################################################################
    # Put file to host with SCP
    # srcFilePath: Local(PC, client) dstFilePath: Server(host)
    def putToHostWithSCP(self, srcFilePath, dstFilePath):
        if self.scp_client == None:
            self.scp_client = SCPClient(self.client.get_transport())
        self.scp_client.put(srcFilePath, dstFilePath)

    ######################################################################
    # Put folder to host with SCP
    # srcFilePath: Local(PC, client) dstFilePath: Server(host)
    def putFolderToHostSCP(self, srcDirPath, dstDirPath):
        if self.scp_client == None:
            self.scp_client = SCPClient(self.client.get_transport())
        self.scp_client.put(srcDirPath, dstDirPath, recursive=True)

    ######################################################################
    # Get folder to host with SCP
    # srcFilePath: Local(PC, client) dstFilePath: Server(host)
    def getFolderFromHostSCP(self, srcDirPath, dstDirPath):
        if self.scp_client == None:
            self.scp_client = SCPClient(self.client.get_transport())
        self.scp_client.get(srcDirPath, dstDirPath, recursive=True)

    ######################################################################
    # Disconnect
    def disconnect(self):
        if self.client != None:
            self.client.close()

        if self.ftp_client != None:
            self.ftp_client.close()

        if self.scp_client != None:
            self.scp_client.close()

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
        ssh.exeCommand('ps -ef > process_list.txt', False)

        # ls-al 명령어로 파일목록 가져오기
        filelist = ssh.exeCommand('ls -al', True)

        for file in filelist:
            # print(file, end='')
            # print(file[:-1])
            ic(file[:-1])

        # Temp 폴더로 이동 후, 파일목록을 가져오기
        # cd temp
        # ls -al

        # 각각 실행 후 터미널이 닫힘
        ssh.exeCommand('cd temp')
        for file in ssh.exeCommand('ls -al', True):
            ic(file[:-1])

        # ; - 앞의 명령어가 실패해도 다음 명령어를 실행
        # && - 앞의 명령어가 성공했을때 다음 명령어가 실행
        # & - 앞의 명령어는 백그라운드로 실행하고 동시에 뒤의 명령어를 실행
        for file in ssh.exeCommand('cd temp;ls -al;pwd', True):
            ic(file[:-1])

        # 쉘 스크립트 파일 생성 후 실행
        ssh.exeCommand('echo "ls -al" > filelist.sh')
        ssh.exeCommand('chmod 777 ./filelist.sh')
        for file in ssh.exeCommand('./filelist.sh', True):
            ic(file[:-1])

        # sudo 실행불가
        ssh.exeCommand('sudo mkdir /mytemp;student;')
        ssh.sudoCommand('mkdir /mytemp')

        ##################################################SFTP##########################################################
        # 서버로 부터 파일 가져오기
        ssh.getFromHost('./process_list.txt', 'process_list.txt')

        # 서버로 파일 올리기
        ssh.putToHost('./process_list.txt', 'process_list_2.txt')

        # 서버에 파일 이름변경하기
        ssh.renameHostFile('./process_list.txt', 'process_list_old.txt') # 파일명 변경
        ssh.renameHostFile('./temp', './temp_old')                       # 폴더명 변경

        # 서버의 파일 삭제
        ssh.deleteHostFile('./process_list_old.txt')

        # 서버의 파일목록 가져오기
        file_list = ssh.getFileListFromHost('./temp_old')
        for file in file_list:
            ic(file)

        # 서버의 파일속성값을 같이 가져오기
        file_list = ssh.getFileAttrListFromHost('./temp_old')
        for file in file_list:
            ic(file)

        # 서버의 폴더삭제
        ssh.deleteHostFolder('./temp_old')

        ###################################################SCP##########################################################
        # 서버로 부터 파일 가져오기(SCP)
        ssh.getFromHostWithSCP('./process_list.txt', 'process_list.txt')

        # 서버로 파일 업로드(SCP)
        ssh.putToHostWithSCP('./process_list.txt', 'process_list_new.txt')

        # 서버에 폴더 업로드(SCP)
        ssh.putFolderToHostSCP('temp', 'temp')

        # 서버에 폴더 다운로드(SCP)
        ssh.getFolderFromHostSCP('temp', 'temp2')
    except Exception as e:
        ic('Exception:', e)
    finally:
        ssh.disconnect()

