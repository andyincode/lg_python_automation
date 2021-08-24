import pyautogui
from pyautogui import *
from icecream import ic
import time

class AutoGui:

    # Screen Size(Only Main Screen)
    def getScreenSize(self):
        screen_size = pyautogui.size()
        return screen_size

    # Current Mouse Position
    def getMousePosition(self):
        current_pos = pyautogui.position()
        return current_pos

    # Check Position Validation
    def isValidPosition(self, pos_x, pos_y):
        valid = pyautogui.onScreen(pos_x, pos_y)
        return valid

    # Set/Get pause time for each call of pyautogui)
    def setPauseTime(self, sec):
        pyautogui.PAUSE = sec

    def getPauseTime(self):
        return pyautogui.PAUSE

    # Fail-Safe : Over FAILSAFE_POINTS and FAILSAFE is True, occurs "pyautogui.FailSafeException", Default:True
    def setFailSafeMode(self, enable):
        # ic(pyautogui.FAILSAFE_POINTS)
        pyautogui.FAILSAFE = enable

    def getFailSafeMode(self):
        return pyautogui.FAILSAFE

    ############################################################################################################
    # 0, 0        X    increases -->
    # +---------------------------+
    # |                           | Y    increases
    # |                           |       |
    # | 1920    x    1080  screen |       |
    # |                           |       V
    # |                           |
    # |                           |
    # +---------------------------+ 1919, 1079

    # Move mouse pointer
    def mouseMove(self, pos_x, pos_y, duration=0, relative=False):
        if relative:
            pyautogui.moveRel(pos_x, pos_y, duration)
        else:
            pyautogui.moveTo(pos_x, pos_y, duration)

    # Drage mouse (현재 위치에서 pox_x, pos_y까지 duration 동안 드래그)
    def mouseDrag(self, pos_x, pos_y, duration=0, relative=False):
        if relative:
            pyautogui.dragRel(float(pos_x), float(pos_y), duration)  # 현재부터 x, y 만큼
        else:
            pyautogui.dragTo(float(pos_x), float(pos_y), duration)   # 현재부터 x, y까지

    # Click mouse (pox_x, pos_y 위치를 interval 간격으로 num_of_click 회 button 클릭)
    def mouseClick(self, pos_x=None, pos_y=None, num_of_click=1, interval=0, button='left', logScreenshot=False):
        pyautogui.click(pos_x, pos_y, num_of_click, interval, button, logScreenshot=logScreenshot)

    def mouseRClick(self, pos_x=None, pos_y=None):
        pyautogui.rightClick(pos_x, pos_y)

    def mouseMClick(self, pos_x=None, pos_y=None):
        pyautogui.middleClick(pos_x, pos_y)

    def mouseDClick(self, pos_x=None, pos_y=None):
        pyautogui.doubleClick(pos_x, pos_y)

    # Vertical Scroll Mouse
    def mouseScrollUp(self, amount):
        pyautogui.scroll(amount)  # amount > 0 : Scroll Up, amount < 0: Scroll Down

    def mouseScrollDown(self, amount):
        pyautogui.scroll(amount * -1)

    # Horizontal Scroll Mouse(Only Mac & Linux)
    def mouseScrollRight(self, amount):
        pyautogui.hscroll(amount)  # amount > 0 : Scroll Right, amount < 0: Scroll Left

    def mouseScrollLeft(self, amount):
        pyautogui.hscroll(amount * -1)

    ############################################################################################################
    # KEY_NAMES (only keyDown, keyUp, pressKey, hotKey)
    # ['\t', '\n', '\r', ' ', '!', '"', '#', '$', '%', '&', "'", '(',
    #  ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7',
    #  '8', '9', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`',
    #  'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    #  'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~',
    #  'accept', 'add', 'alt', 'altleft', 'altright', 'apps', 'backspace',
    #  'browserback', 'browserfavorites', 'browserforward', 'browserhome',
    #  'browserrefresh', 'browsersearch', 'browserstop', 'capslock', 'clear',
    #  'convert', 'ctrl', 'ctrlleft', 'ctrlright', 'decimal', 'del', 'delete',
    #  'divide', 'down', 'end', 'enter', 'esc', 'escape', 'execute', 'f1', 'f10',
    #  'f11', 'f12', 'f13', 'f14', 'f15', 'f16', 'f17', 'f18', 'f19', 'f2', 'f20',
    #  'f21', 'f22', 'f23', 'f24', 'f3', 'f4', 'f5', 'f6', 'f7', 'f8', 'f9',
    #  'final', 'fn', 'hanguel', 'hangul', 'hanja', 'help', 'home', 'insert', 'junja',
    #  'kana', 'kanji', 'launchapp1', 'launchapp2', 'launchmail',
    #  'launchmediaselect', 'left', 'modechange', 'multiply', 'nexttrack',
    #  'nonconvert', 'num0', 'num1', 'num2', 'num3', 'num4', 'num5', 'num6',
    #  'num7', 'num8', 'num9', 'numlock', 'pagedown', 'pageup', 'pause', 'pgdn',
    #  'pgup', 'playpause', 'prevtrack', 'print', 'printscreen', 'prntscrn',
    #  'prtsc', 'prtscr', 'return', 'right', 'scrolllock', 'select', 'separator',
    #  'shift', 'shiftleft', 'shiftright', 'sleep', 'space', 'stop', 'subtract', 'tab',
    #  'up', 'volumedown', 'volumemute', 'volumeup', 'win', 'winleft', 'winright', 'yen',
    #  'command', 'option', 'optionleft', 'optionright']
    # pyautogui.KEY_NAMES

    # Type Keyboard (interval 간격으로 한글자씩 text 타이핑)
    def kbWrite(self, text, interval=0, logScreenshot=False):
        pyautogui.write(text, interval, logScreenshot=logScreenshot)

    # Press Keyboard key in KEY_NAMES
    def kbPressKey(self, key_name, presses=1, interval=0):
        pyautogui.press(key_name, presses, interval)

    # Press key combination
    def kbHotKey(self, *args, **kwargs):
        pyautogui.hotkey(*args, **kwargs)

    # Keep press key-down until call key-up
    def kbKeyDown(self, key_name):
        pyautogui.keyDown(key_name)

    # Release key-down
    def kbKeyUp(self, key_name):
        pyautogui.keyUp(key_name)

    # ScreenShot (Save to file or return as Image object of pillow
    def screenshot(self, file_name=None):
        img = pyautogui.screenshot(file_name)
        return img

    # Get Image location in screen
    def getPositionOfImage(self, image_path, is_center=False, is_fast_mode=False):
        position = pyautogui.locateOnScreen(image_path, grayscale=is_fast_mode)

        if position is not None:
            if is_center:
                position = pyautogui.center(position)
            else:
                position = Point(position.left, position.top)
            return position
        else:
            return position

        # Use function
        # if is_center:
        #     position = pyautogui.locateCenterOnScreen(image_path, grayscale=is_fast_mode)
        # else:
        #     position = pyautogui.locateOnScreen(image_path, grayscale=is_fast_mode)
        # return position

    def getPositionListOfImage(self, image_path, is_center=False, is_fast_mode=False):
        positions = list(pyautogui.locateAllOnScreen(image_path, grayscale=is_fast_mode))

        position_list = []
        for position in positions:
            if is_center:
                position_list.append(pyautogui.center(position))
            else:
                position_list.append(Point(position.left, position.top))
        return position_list

    # Click Image
    def clickImage(self, file_name):
        pyautogui.click(file_name)

if __name__ == "__main__":
    # Create Object
    ag = AutoGui()

    # # Get Screen Size
    # ic(ag.getScreenSize())
    #
    # # Get Current Mouse Position
    # ic(ag.getMousePosition())
    #
    # # Check Position Validation
    # ic(ag.isValidPosition(100, 100))
    # ic(ag.isValidPosition(4000, 4000))
    # ic(ag.isValidPosition(1920, 1080))
    # ic(ag.isValidPosition(-1, -1))
    # ic(ag.isValidPosition(0, 0))
    # ic(ag.isValidPosition(1919, 1079))
    #
    # # Set Pause Time for each call function
    # ic('Default Pause Time:', ag.getPauseTime())
    # ag.setPauseTime(1)
    # ic('New Pause Time:', ag.getPauseTime())
    # ag.setPauseTime(0.1)
    #
    # # Set Fail-Safe Mode
    # ic('Default Fail-Safe Mode:', ag.getFailSafeMode())
    # ag.setFailSafeMode(False)
    # ic('New Fail-Safe Mode:', ag.getFailSafeMode())

    ag.setFailSafeMode(False)
    ag.setPauseTime(1)

    # # Mouse Move
    # ag.mouseMove(0, 0)  # 0, 0
    # ag.mouseMove(1000, 1000, 5)  # 500, 500
    # ag.mouseMove(-500, -500, 5, True)  # 400, 400

    # # Mouse Drag
    # ag.mouseDrag(300, 300, 2)            # 현재위치에서 300, 300 위치까지 Drag
    # ag.mouseDrag(300.0, 300.0, 2, True)  # 현재위치에서 100, 100 만틈만 Drag

    # # Mouse Click
    # time.sleep(3)
    # position = ag.getMousePosition()  # 계산기 키패드 위치가져오기
    # ag.mouseClick(position.x, position.y)  # Click Left Button
    # ag.mouseClick(position.x, position.y, 10, 1, 'left', True)  # Click button 10 times at 1 sec interval and screenshot
    # ag.mouseDClick(position.x, position.y)  # Double Click
    # ag.mouseRClick(position.x, position.y)  # Click Right Button

    # # Mouse Scroll
    # ag.mouseScrollUp(1000)
    # ag.mouseScrollDown(1000)

    # # KB Write
    # ag.kbWrite('Hello')
    # ag.kbWrite('Hello', 1, True)  # 5초간격으로 Hello를 한글자씩 입력후 스크린샷

    # KB PresseKey
    # ag.kbPressKey('win')  # Win키
    # ag.kbPressKey('num0', 10, 1)  # 1초 간격으로 0을 10번 입력

    # # KG Hotkey
    # ag.kbHotKey('ctrl', 'shift', 'esc')  # 작업관리자

    # # Keboard Key Down/Up
    # ag.kbKeyDown('ctrl')
    # ag.kbKeyDown('shift')
    # ag.kbKeyDown('esc')
    # ag.kbKeyUp('esc')
    # ag.kbKeyUp('shift')
    # ag.kbKeyUp('ctrl')
