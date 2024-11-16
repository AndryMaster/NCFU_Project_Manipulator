import time
import serial
import keyboard

from key_board import *
from config import *
from utils import *
from msg import *


def pack_msg(msg):
    try:
        return str(msg).encode('ascii')
    except Exception as e:
        raise TypeError(f"Incorrect type of {msg} {type(msg)}\n{e}")


def send_msg(port: serial.Serial, msg, debug=False):
    global LAST_SEND
    if LAST_SEND is None or time.time() - LAST_SEND >= SEND_DELAY:
        if len(msg := pack_msg(msg)):
            port.write(msg)
            LAST_SEND = time.time()
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


def send_msg_late(port: serial.Serial, wait_sec: float, msg, debug=False):
    time.sleep(wait_sec)
    send_msg(port, msg, debug=debug)


def print_cur_pos(port=None):
    print(f'Current Pos: {CUR_POS}')
    # if port: else:


def press_key(port: serial.Serial):
    # print("Pressing key...")
    send_msg(port, MsgOne(0, 10))
    time.sleep(1.35)
    send_msg(port, MsgOne(0, CUR_POS[0]))
    # send_msg_late(port, 0., MsgOne(0, 0))
    # send_msg_late(port, 1.6, MsgOne(0, CUR_POS[0]))


def move_to_key(event: keyboard.KeyboardEvent, port: serial.Serial, debug=False):
    key = event.name.lower()
    if key in RUS_KEYS:
        kb_config = KB_CONFIG_RUS
    elif key in ENG_KEYS:
        kb_config = KB_CONFIG_ENG
    else:
        return

    send_msg(port, MsgAll(kb_config[key]))

    if debug:
        print(f'Moving to key: {event.name}')


def control_with_keys(event: keyboard.KeyboardEvent, port: serial.Serial, debug=False):
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

    while True:
        if keyboard.is_pressed('esc'):
            break

        get_msg_all(port, is_print=True)

        line = input("Command in<: ")
        send_msg(port, line, debug=debug)
        time.sleep(0.1)


def mode_control(port: serial.Serial, debug: bool):
    print(INFO_TEXT["mode_control"])

    keyboard.on_press_key('enter', lambda event: print_cur_pos(port))
    keyboard.on_press_key('p', lambda event: press_key(port))
    # keyboard.on_press_key('+', lambda event: save_key())
    for key in ALL_CONTROL_KEYS:
        keyboard.on_press_key(key, lambda event: control_with_keys(event, port))

    # for key in RUS_KEYS:
    #     keyboard.on_press_key(key, lambda event: move_to_key(event, port))

    while True:
        if keyboard.is_pressed('esc'):
            break

        get_msg_all(port, is_print=True)


def mode_text_printing(port: serial.Serial, debug: bool):
    print(INFO_TEXT["mode_print_text"])

    while True:
        if keyboard.is_pressed('esc'):
            break

        while True:  # get lang mode
            try:
                mode_lang = int(input(INFO_TEXT["select_print_text"]))
                print()
                if mode_lang in [1, 2]:
                    break
            except Exception as e:
                continue

        if mode_lang == 1:
            kb_config = KB_CONFIG_RUS
        else:
            kb_config = KB_CONFIG_ENG

        line = input("Text in<: ").lower()
        print()
        err_chars = set(line) - set(kb_config.keys())
        if len(err_chars) > 0:
            print(f"Invalid chars: [ {''.join(err_chars)} ]")
        else:
            for char in line:
                send_msg(port, MsgAll(kb_config[char]))  # To CHAR
                time.sleep(3.1)
                press_key(port)                          # Press CHAR
                time.sleep(0.7)
                send_msg(port, MsgAll([90] * 4))         # To START
                time.sleep(2.5)


def main(port: serial.Serial, debug: bool):
    print(INFO_TEXT["main"])

    # Arduino init
    print("Please wait...\n")
    send_msg(port, "Try start")
    time.sleep(3)
    send_msg(port, "Try start")
    time.sleep(0.5)
    get_msg_all(port)

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
            # test(port, debug)
            continue
        break


if __name__ == '__main__':
    port_ = serial.Serial(PORT, SERIAL_SPEED)
    main(port_, debug=True)
