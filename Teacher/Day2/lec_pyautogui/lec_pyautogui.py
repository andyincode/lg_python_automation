import pyautogui
from pyautogui import *

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
        pyautogui.PAUSE = 2

    def getPauseTime(self):
        return pyautogui.PAUSE

    # Fail-Safe : Over FAILSAFE_POINTS and FAILSAFE is True, occurs "pyautogui.FailSafeException", Default:True
    def setFailSafeMode(self, enable):
        # ic(pyautogui.FAILSAFE_POINTS)
        pyautogui.FAILSAFE = enable

    def getFailSafeMode(self):
        return pyautogui.FAILSAFE