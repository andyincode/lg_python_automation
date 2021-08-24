from pynput import mouse
from pynput.mouse import Button

def on_move(x, y):
    # print('Pointer moved to {0}'.format((x,y)))
    pass

def on_click(x, y, button, pressed):
    print('Mouse Clicked position: (%s, %s)' % (x, y))
    print('Button: %s' % button)
    print('Pressed: %s' % pressed)

    if button == Button.right and not pressed:
        return False

def on_scroll(x, y, dx, dy):
    print('Scrolled {0} at {1}'.format('down' if dy < 0 else 'up', (x, y)))
    print('Scrolled {0} at {1}'.format('left' if dx < 0 else 'right', (x, y)))

# with mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll) as listener:
#     listener.join()

listener = mouse.Listener(on_move=on_move, on_click=on_click, on_scroll=on_scroll)
listener.start()
listener.join()
