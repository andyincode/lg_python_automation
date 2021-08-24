from lec_pyserial_class import MySerial
import json
from datetime import datetime
from icecream import ic

# 01. 전원 (Command: k a)
# ▶ 세트의 전원 켜짐/ 꺼짐을 제어합니다.
# Transmission
# [k][a][ ][Set ID][ ][Data][Cr]
# Data	00: 꺼짐
# 01: 켜짐
# ex) ka 01 01, ka 01 00, ka 01 ff
# Acknowledgement
# [a][ ][Set ID][ ][OK/NG][Data][x]
# ex) a 01 OK01x, a 01 OK00x, a 01 NG11x
# * 디스플레이의 전원이 완전히 켜진 이후에 정상적인 Acknowledgement 신호가 돌아옵니다.
#
# ** Transmission/ Acknowledgement 신호 사이에는 일정시간 지연이 발생할 수 있습니다.

power_status = '00' # 기본값은 Power Off
is_power_on = False

ser = MySerial()
ser.openSerial('com2')

# a = True
# if a == True: ==> if a is True:

ic('Program is started...')
while True:
    readed = ser.readUntilExitCode(b'\x0d')

    # 읽어온 데이터 출력
    ic('Readed byte string:', readed)

    # byte타입의 읽어온 데이터를 unicode(문자열)로 decoding
    # 문자열로 디코딩해야만 문자열 관련 함수 사용가능
    readed = readed.decode()

    # Unocode 문자열 출력
    ic('Readed byte string:', readed)

    # 프로그램 종료조건 'exit' 문자열 비교
    # EXIT, Exit, exit, ...
    if readed.lower() == 'exit':
        ser.close()
        break

    datalist = readed.split(' ')
    if not (len(readed) == 8 and len(datalist) == 3):
        ic('Wrong Command Format!!!')
        ser.writePortUnicode('Wrong Command Format!!!\r\n')
        continue

    # ka 01 00 : Power Off
    command = datalist[0].lower() # KA, ka , Ka, kA
    setId = datalist[1]
    value = datalist[2].lower() # FF, ff

    # Power Off
    if value == '00':
        is_power_on = False
        response = '%s%sx' % ('OK', value) # OK00x
        ic('Changed PowerStatus:', is_power_on)
    # Power On
    elif value == '01':
        is_power_on = True
        response = '%s%sx' % ('OK', value)  # OK01x
        ic('Changed PowerStatus:', is_power_on)
    # Check Power Status
    elif value == 'ff':
        if is_power_on is True:
            response = 'OK01x'
        else:
            response = 'OK00x'
        # reponse = '%s%sx' % ('OK', '01' if is_power_on else '00')
        ic('Current PowerStatus:', is_power_on)
    else:
        response = '%s%sx' % ('NG', value) # NGXXx

    response = '%s %s %s\r\n' % (command[1], setId, response) # a 01 OK01x

    jsonData = {'command':command, 'setId':setId, 'value':value, 'response':response[:9+1]}
    jsonString = json.dumps(jsonData)
    ic(jsonString)
    now = datetime.now().strftime('[%Y-%m-%d %H:%M:%S] ')

    with open('command.log', 'a', encoding='utf8') as f:
        f.write(now + jsonString + '\n')

    ser.writePortUnicode(response)
ic('Done')


