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

    return ser

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

# EOF 만날때까지 Read, Putty의 경우 EOF는 Ctrl + J
def readEOF(ser):
    readed = ser.readline()
    return readed[:-1]

# Exit code인 Ctrl + C 이 들어올때까지 Read
def readUntilExitCode(ser, code=b'\x03'):
    readed = b''
    while True:
        data = ser.read() # size default: 1
        ic(data)
        readed += data
        if data == code:
            return readed[:-1]


# 이코드가 의미하는것은 이 파일 즉 lec_serial.py 모듈을 실행했을때 들어오는 코드
# ic(__name__)
if __name__ == '__main__':
    # 객체생성
    ser = openSerial('com2')

    # 영문쓰기
    string = 'Hello World\r\n'
    # writePort(ser, string.encode())
    writePortUnicode(ser, string)

    # 한글쓰기
    string = '안녕 세상아\r\n'
    writePortUnicode(ser, string)

    # Read 1 byte: 1byte만 읽고 return
    ic(read(ser))

    # Read 5 byte: 5byte만 읽고 return
    ic(read(ser, 5))
    ic(read(size=5, ser=ser))

    # Read with timeout 5 sec: 5초 대기후에 데이터가 없으면 return
    ic(read(ser, 1, 5))

    # Read Until EOF
    ic(readEOF(ser))

    # Read Until EOF with Hangul
    ic(readEOF(ser).decode())

    # Read until exit code (Ctrl + C)
    ic(readUntilExitCode(ser))