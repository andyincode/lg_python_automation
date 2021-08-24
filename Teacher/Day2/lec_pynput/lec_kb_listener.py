from pynput import keyboard
from pynput.keyboard import Key
# pyqutogui module
# https://pyautogui.readthedocs.io/en/latest/index.html
# https://www.autohotkey.com/
# https://www.autoitscript.com/site/

def on_press(key):
    print('Key %s press' % key)
    with open('../key.log', 'a', encoding='utf8') as f:
        try:
            f.write('Key %s preesed\n' % key.char)
        except:
            f.write('Key %s pressed\n' % key)

def on_release(key):
    print('Key %s release' % key)
    with open('../key.log', 'a', encoding='utf8') as f:
        try:
            f.write('Key %s release\n' % key.char)
        except:
            f.write('Key %s release\n' % key)

    if key == Key.esc:
        return False

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    print('Keyboard is listening...')
    listener.join()

# listener = keyboard.Listener(on_press=on_press, on_release=on_release)
# listener.start()
# listener.join()

print("Keyboard's listener is dead!")
