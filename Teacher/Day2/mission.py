from lec_pyautogui.lec_pyautogui import AutoGui
import time
import pyperclip
from datetime import datetime
#
# with open('pw.txt', 'r') as f:
#     password = f.readline()
password = ''

# 객체생성
ag = AutoGui()

# Interval 타임 2초 설정
ag.setPauseTime(2)

# # 크롬브라우저를 네이버 홈페이지로 실행
# ag.kbHotKey('win', 'r')
# ag.kbWrite('chrome www.naver.com\n')
# time.sleep(3)
# ag.clickImage('naver_login.png')

# # ID/PW 입력
# ag.kbWrite('eliaskis')
# ag.kbPressKey('tab')
# ag.kbWrite(password + '\n')

# # pyperclip을 이용해서 ctrl+c, ctrl+v
# pyperclip.copy('eliaskis')
# ag.kbHotKey('ctrl', 'v')
# ag.kbPressKey('tab')
# pyperclip.copy(password)
# ag.kbHotKey('ctrl', 'v')
# ag.kbPressKey('enter')

# # 한글자씩 딜레이를 두고 입력
# for key in 'eliaskis':
#     ag.kbWrite(key)
# ag.kbPressKey('tab')
# for key in password:
#     ag.kbWrite(key)
# ag.kbPressKey('enter')

# 네이버 스토어를 경유하여 로그인
ag.kbHotKey('win', 'r')

ag.kbWrite('chrome https://sell.smartstore.naver.com/#/naverpay/sale/delivery\n')
time.sleep(3)
ag.clickImage('naver_login2.png')

ag.kbWrite('eliaskis')
ag.kbPressKey('tab')
ag.kbWrite(password + '\n')

ag.kbHotKey('alt', 'd')
ag.kbWrite('www.naver.com\n')

# 방법1
# ag.kbWrite('코로나 현황') # 안됨

# 방법2
# ag.kbPressKey('hangul')
# ag.kbWrite('zhfhsk gusghkd\n')
# ag.kbPressKey('hangul')

# 방법3
pyperclip.copy('코로나 현황')
ag.kbHotKey('ctrl', 'v')
ag.kbPressKey('enter')

now = datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
ag.screenshot('%s.png' % now)
