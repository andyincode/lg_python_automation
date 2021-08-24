import pyautogui
from pyautogui import *
from icecream import ic

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
            pyautogui.dragRel(float(pos_x), float(pos_y), duration)  # 현재부터 x, y까지
        else:
            pyautogui.dragTo(float(pos_x), float(pos_y), duration)  # 현재부터 x, y 만큼

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

if __name__ == "__main__":
    # Create Object
    ag = AutoGui()

    # Get Screen Size
    ic(ag.getScreenSize())

    # Get Current Mouse Position
    ic(ag.getMousePosition())

    # Check Position Validation
    ic(ag.isValidPosition(100, 100))
    ic(ag.isValidPosition(4000, 4000))
    ic(ag.isValidPosition(1920, 1080))
    ic(ag.isValidPosition(-1, -1))
    ic(ag.isValidPosition(0, 0))
    ic(ag.isValidPosition(1919, 1079))

    # Set Pause Time for each call function
    ic('Default Pause Time:', ag.getPauseTime())
    ag.setPauseTime(1)
    ic('New Pause Time:', ag.getPauseTime())
    ag.setPauseTime(0.1)

    # Set Fail-Safe Mode
    ic('Default Fail-Safe Mode:', ag.getFailSafeMode())
    ag.setFailSafeMode(False)
    ic('New Fail-Safe Mode:', ag.getFailSafeMode())