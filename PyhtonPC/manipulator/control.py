import time
import keyboard
from config import *


# def set_is_control(event: keyboard.KeyboardEvent):
#     global IS_CONTROL, IS_CHANGED, CUR_POS
#     IS_CONTROL = not IS_CONTROL
#     if IS_CONTROL:
#         IS_CHANGED = True
#         CUR_POS = [90] * 4
#         print(f'Control ON ({CUR_POS})')
#         # send_msg(port, MsgAll(CUR_POS))
#     else:
#         print('Control OFF')
#
#
# def print_cur_pos(event: keyboard.KeyboardEvent):
#     if IS_CONTROL:
#         print(f'Current Pos: {CUR_POS} ({IS_CHANGED})')
#
#
# def control_with_keys(event: keyboard.KeyboardEvent):
#     global IS_CONTROL, IS_CHANGED, CUR_POS
#     # print(f'{IS_CONTROL} {event.name} {event.event_type}')
#     if not IS_CONTROL:
#         return
#
#     for key, item in CONTROL.items():
#         add_val = ADD_POS[key]
#         if keyboard.is_pressed(MUL_POS['key']):
#             add_val *= MUL_POS['mul']
#
#         if event.name in item['keys']:
#             if event.name == item['keys'][0]:
#                 add_val *= -1
#             if keyboard.is_pressed('ctrl') == item['ctrl_pos']:
#                 CUR_POS[key] = clip(CUR_POS[key] + add_val)
#                 IS_CHANGED = True


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

    keyboard.on_press_key('f2', set_is_control)
    keyboard.on_press_key('enter', print_cur_pos)

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

