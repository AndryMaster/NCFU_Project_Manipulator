import time
import serial
import keyboard

from config import *
from msg import *
# from control import set_is_control, print_cur_pos, control_with_keys


def pack_msg(_msg):
    try:
        return str(_msg).encode('ascii')
    except Exception as e:
        raise TypeError(f"Incorrect type of {_msg} {type(_msg)}\n{e}")


def send_msg(port: serial.Serial, msg, debug=DEBUG):
    if len(msg := pack_msg(msg)):
        port.write(msg)
    if debug:
        print(f"Sending message: {msg}")


def get_msg_all(port: serial.Serial, debug=DEBUG):
    try:
        if port.in_waiting > 0:
            text = port.read(port.in_waiting).decode('cp1251')  # .decode('ascii')
            if debug:
                print(f"Out>: {text.strip()}")
            return text
    except Exception as e:
        print(f'Error: {e}')
        return str(e)
    # while port.in_waiting > 0:
    #     try:
    #         line = port.readline().decode('ascii')
    #         print(line)
    #     except Exception as e:
    #         pass
    # return line


def set_is_control(event: keyboard.KeyboardEvent):
    global IS_CONTROL, IS_CHANGED, CUR_POS
    IS_CONTROL = not IS_CONTROL
    if IS_CONTROL:
        IS_CHANGED = True
        CUR_POS = [90] * 4
        print(f'Control ON ({CUR_POS})')
        # send_msg(port, MsgAll(CUR_POS))
    else:
        print('Control OFF')


def print_cur_pos(event: keyboard.KeyboardEvent):
    if IS_CONTROL:
        print(f'Current Pos: {CUR_POS} ({IS_CHANGED})')


def control_with_keys(event: keyboard.KeyboardEvent, debug=DEBUG):
    global IS_CONTROL, IS_CHANGED, CUR_POS
    # print(f'{IS_CONTROL} {event.name} {event.event_type}')
    if not IS_CONTROL:
        return
    IS_CHANGED = False

    event.name = event.name.lower()
    for key, item in CONTROL.items():

        add_val = MULTY_ADD_POS['else'][key]
        for modifier in MULTY_ADD_POS.keys():
            if modifier != 'else' and keyboard.is_pressed(modifier):
                add_val = MULTY_ADD_POS[modifier][key]
                break

        if event.name in item['keys']:
            if event.name == item['keys'][0]:
                add_val *= -1
            if keyboard.is_pressed('ctrl') == item['ctrl_pos']:
                CUR_POS[key] = clip(CUR_POS[key] + add_val)
                IS_CHANGED = True
                send_msg(port, MsgAll(CUR_POS))

    if debug:
        print(f'Key: {IS_CHANGED} {event.name} {event.event_type}')


def main(port: serial.Serial):
    global IS_CHANGED
    # print(f"Control speed: {[e / CYCLE_TIME for e in ADD_POS]} deg/sec")

    # Events
    keyboard.on_press_key('f2',    set_is_control)
    keyboard.on_press_key('enter', print_cur_pos)

    keyboard.on_press_key('up',    control_with_keys)
    keyboard.on_press_key('down',  control_with_keys)
    keyboard.on_press_key('left',  control_with_keys)
    keyboard.on_press_key('right', control_with_keys)
    keyboard.on_press_key('w',     control_with_keys)
    keyboard.on_press_key('a',     control_with_keys)
    keyboard.on_press_key('s',     control_with_keys)
    keyboard.on_press_key('d',     control_with_keys)

    while True:
        if keyboard.is_pressed('esc'):
            break

        get_msg_all(port, debug=(not IS_CONTROL))

        # Control
        if IS_CONTROL:
            pass
            # if IS_CHANGED:
            #     print('seng change')
            #     send_msg(port, MsgAll(CUR_POS))
            #     IS_CHANGED = False
        else:
            line = input("Command in<: ")
            # Check line
            send_msg(port, line)


if __name__ == '__main__':
    DEBUG = True
    IS_CONTROL = False
    port = serial.Serial(PORT, SERIAL_SPEED)
    main(port)
    # test1()
