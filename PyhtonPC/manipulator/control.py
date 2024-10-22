import time
import keyboard
from config import *


def set_actual(event):
    global IS_CONTROL
    IS_CONTROL = not IS_CONTROL
    if IS_CONTROL:
        print('Control ON')

    else:
        print('Control OFF')


def get_current_position(event):
    print(CUR_POS)


if __name__ == "__main__":
    CYCLE_TIME = 50e-3
    IS_CONTROL = False
    CUR_POS = [90] * 4
    ADD_POS = [2, 2, 2, 2]
    CONTROL = {
        0: 'w s'.split(),
        1: 'up down'.split(),
        2: 'left right'.split(),
        3: 'a d'.split(),
    }

    keyboard.on_press_key('f2', set_actual)
    keyboard.on_press_key('enter', get_current_position)

    while True:
        if keyboard.is_pressed('esc'):
            break

        # Control
        if IS_CONTROL:
            for key, val in CONTROL.items():
                val_pressed = [keyboard.is_pressed(v) for v in val]
                if val_pressed[0] and not val_pressed[1]:
                    CUR_POS[key] = clip(CUR_POS[key] + ADD_POS[key])
                elif not val_pressed[0] and val_pressed[1]:
                    CUR_POS[key] = clip(CUR_POS[key] - ADD_POS[key])

            time.sleep(CYCLE_TIME)

        else:
            line = input("Command in<: ")

