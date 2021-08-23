import serial
from icecream import ic

##############################################################################################
# 시리얼 포트 열기
##############################################################################################
def openSerial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtscts=False, dsrdtr=False):
    # 시리얼객체 생성
    ser = serial.Serial()

    # 시리얼포트 설정
    ser.port = port
    ser.baudrate = baudrate
    ser.bytesize = bytesize
    ser.parity = parity
    ser.stopbits = stopbits
    ser.timeout = timeout
    ser.xonoff = xonxoff
    ser.rtscts = rtscts
    ser.dsrdtr = dsrdtr

    # 시리얼포트 열기
    ser.open()
    # ser = serial.Serial(port, baudrate, ...) # open() 콜할 필요없음.

##############################################################################################
# 시리얼 포트 쓰기
##############################################################################################
def writePort(ser, data):
    ser.write(data)

def writePortUnicode(ser, data):    # 유니코드 인자를 받아서 bytes 타입으로 변환후 write
    ser.write(data.encode())

##############################################################################################
# 시리얼 포트 읽기
##############################################################################################
# size 만큼 timeout 대기 후 read
def read(ser, size=1, timeout=None):
    ser.timeout = timeout
    readed = ser.read(size)
    return readed

# EOF 만날때까지 Read
def readEOF(ser):
    readed = ser.readline()
    return readed

# Exit code인 Ctrl + C 이 들어올때까지 Read
def readUntilExitCode(ser, code=b'\x03'):
    readed = b''
    while True:
        data = ser.read() # size default: 1
        ic(data)
        readed += data
        if data == code:
            return readed

ic(__name__)
# if __name__ == '__main__':
#     pass

ser = openSerial('com3')

