import time
import serial
import keyboard

from config import *
from msg import *


def pack_msg(msg):
    try:
        return str(msg).encode('ascii')
    except Exception as e:
        raise TypeError(f"Incorrect type of {msg} {type(msg)}\n{e}")


def send_msg(port: serial.Serial, msg, debug=False):
    if len(msg := pack_msg(msg)):
        port.write(msg)
    if debug:
        print(f"Sending message: {msg}")


def get_msg_all(port: serial.Serial, is_print=False):
    encoding = 'cp1251'  # 'ascii'
    try:
        if port.in_waiting > 0:
            text = port.read(port.in_waiting).decode(encoding)
            if is_print:
                print(f"Out>: {text.strip()}\n")
            return text
    except Exception as e:
        print(f'Error: {e}')
    # while port.in_waiting > 0:
    #     try:
    #         line = port.readline().decode(encoding)
    #         print(f"Out>: {line.strip()}\n")
    #     except Exception as e:
    #         print(f'Error: {e}')


def print_cur_pos(port=None):
    if port:
        print(f'Current Pos: {CUR_POS}')
    else:
        print(f'Current Pos: {CUR_POS}')


def control_with_keys(event: keyboard.KeyboardEvent, port: serial.Serial, debug=DEBUG):
    event.name = event.name.lower()
    for key, item in CONTROL.items():

        add_val = MULTY_ADD_POS['default'][key]
        for modifier in MULTY_ADD_POS.keys():
            if modifier != 'default' and keyboard.is_pressed(modifier):
                add_val = MULTY_ADD_POS[modifier][key]
                break

        if event.name in item['keys']:
            if event.name == item['keys'][0]:
                add_val *= -1
            CUR_POS[key] = clip(CUR_POS[key] + add_val)
            send_msg(port, MsgAll(CUR_POS))

    if debug:
        print(f'Key: {event.name} pressed ({add_val} deg)')


def mode_cli(port: serial.Serial, debug: bool):
    print(INFO_TEXT["mode_cli"])

    send_msg(port, 'Hello', debug=debug)
    while True:
        if keyboard.is_pressed('esc'):
            break

        get_msg_all(port, is_print=True)

        line = input("Command in<: ")
        send_msg(port, line, debug=debug)


def mode_control(port: serial.Serial, debug: bool):
    print(INFO_TEXT["mode_cli"])

    # f_mask = lambda event: control_with_keys(event, port)
    # keyboard.on_press_key('up', f_mask)
    keyboard.on_press_key('enter', lambda event: print_cur_pos(port))
    for key in ALL_KEYS:
        keyboard.on_press_key(key, lambda event: control_with_keys(event, port))

    send_msg(port, 'Hello', debug=debug)
    while True:
        if keyboard.is_pressed('esc'):
            break

        get_msg_all(port, is_print=True)


def mode_text_printing(port: serial.Serial, debug: bool):
    print(INFO_TEXT["mode_print_text"])
    send_msg(port, 'Hello', debug=debug)

    while True:
        if keyboard.is_pressed('esc'):
            break


def main(port: serial.Serial, debug: bool):
    print(INFO_TEXT["main"])
    while True:
        try:
            mode = int(input("Input mode: "))
            print()
        except Exception as e:
            continue

        if mode == 1:
            mode_cli(port, debug)
        elif mode == 2:
            mode_control(port, debug)
        elif mode == 3:
            mode_text_printing(port, debug)
        else:
            continue
        break


if __name__ == '__main__':
    DEBUG = False
    port_ = serial.Serial(PORT, SERIAL_SPEED)
    main(port_, DEBUG)
