import serial

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
    pass

##############################################################################################
# 시리얼 포트 읽기
##############################################################################################
def read(ser, size=1, timeout=None):
    pass

