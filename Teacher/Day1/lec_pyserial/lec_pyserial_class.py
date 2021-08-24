import serial
from icecream import ic

class MySerial:
    def __init__(self, port=None):
        self.ser = None

        if port is not None:
            self.openSerial(port)

        self.is_power_on = False

    ##############################################################################################
    # 시리얼 포트 열기
    ##############################################################################################
    def openSerial(self, port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                   stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False):
        # 시리얼객체 생성
        self.ser = serial.Serial()

        # 시리얼포트 설정
        self.ser.port = port
        self.ser.baudrate = baudrate
        self.ser.bytesize = bytesize
        self.ser.parity = parity
        self.ser.stopbits = stopbits
        self.ser.timeout = timeout
        self.ser.xonoff = xonxoff
        self.ser.rtscts = rtscts
        self.ser.dsrdtr = dsrdtr

        # 시리얼포트 열기
        self.ser.open()

    ##############################################################################################
    # 시리얼 포트 쓰기
    ##############################################################################################
    def writePort(self, data):
        self.ser.write(data)

    def writePortUnicode(self, data):  # 유니코드 인자를 받아서 bytes 타입으로 변환후 write
        self.ser.write(data.encode())

    ##############################################################################################
    # 시리얼 포트 읽기
    ##############################################################################################
    # size 만큼 timeout 대기 후 read
    def read(self, size=1, timeout=None):
        self.ser.timeout = timeout
        readed = self.ser.read(size)
        return readed

    # EOF 만날때까지 Read, Putty의 경우 EOF는 Ctrl + J
    def readEOF(self):
        readed = self.ser.readline()
        return readed[:-1]

    # Exit code인 Ctrl + C 이 들어올때까지 Read
    def readUntilExitCode(self, code=b'\x03'):
        readed = b''
        while True:
            data = self.ser.read()  # size default: 1
            ic(data)
            readed += data
            if data == code:
                return readed[:-1]

if __name__ == '__main__':
    # 객체생성
    ser = MySerial('com2')

    # 영문쓰기
    string = 'Hello World\r\n'
    # writePort(ser, string.encode())
    ser.writePortUnicode(string)

    # 한글쓰기
    string = '안녕 세상아\r\n'
    ser.writePortUnicode(string)

    # Read 1 byte: 1byte만 읽고 return
    ic(ser.read())

    # Read 5 byte: 5byte만 읽고 return
    ic(ser.read(5))
    ic(ser.read(size=5))

    # Read with timeout 5 sec: 5초 대기후에 데이터가 없으면 return
    ic(ser.read(1, 5))

    # Read Until EOF (Ctrl + J)
    ic(ser.readEOF())

    # Read Until EOF with Hangul
    ic(ser.readEOF().decode())

    # Read until exit code (Ctrl + C)
    ic(ser.readUntilExitCode())


