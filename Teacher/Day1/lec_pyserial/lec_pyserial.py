import serial

##############################################################################################
# 시리얼 포트 열기
##############################################################################################
def openSerial(port, baudrate=9600, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
               stopbits=serial.STOPBITS_ONE, timeout=None, xonxoff=False, rtccts=False, dsrdtr=False):
    pass