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
    if port:
        print(f'Current Pos: {CUR_POS}')
    else:
        print(f'Current Pos: {CUR_POS}')


def press_key(port: serial.Serial):
    print("Pressing key...")
    pos = CUR_POS[0]
    send_msg_late(port, 0., MsgOne(0, 0))
    send_msg_late(port, 1.6, MsgOne(0, pos))


# def save_key():
#     print("Saving key...")
#     key = input("Key: ").lower()  # keyboard.read_key().strip().lower()
#     print(key, CUR_POS)
#     if len(key) == 1:
#         with open('k.txt', 'w') as f:
#             f.write(f'{key};{" ".join(map(str, CUR_POS))}\n')


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

    while True:
        if keyboard.is_pressed('esc'):
            break

        get_msg_all(port, is_print=True)


def mode_text_printing(port: serial.Serial, debug: bool):
    print(INFO_TEXT["mode_print_text"])

    while True:
        if keyboard.is_pressed('esc'):
            break

        line = input("Text in<: ").lower()
        for char in line:
            if char in RUS_KEYS:
                kb_config = KB_CONFIG_RUS
            elif char in ENG_KEYS:
                kb_config = KB_CONFIG_ENG
            else:
                print(f"Invalid char {char}")
                continue
            send_msg(port, MsgAll(kb_config[char]))
            time.sleep(3)
            press_key(port)
            time.sleep(1)
            send_msg(port, MsgAll([90] * 4))
            time.sleep(3)


# def test(port: serial.Serial, debug: bool):
#     send_msg(port, 'Hello', debug=debug)
#
#     t1 = time.time()
#     msg_late_task(port, 2000, MsgOne(0, 90))
#     msg_late_task(port, 2000, MsgAll([120, 95, 85, 60]))
#     print(f"{time.time() - t1} seconds")
#     msg_late_task(port, 2000, MsgAll([120, 95, 85, 60]))
#     print(f"{time.time() - t1} seconds")
#     msg_late_task(port, 2000, MsgAll([20, 90, 90, 90]))
#     print(f"{time.time() - t1} seconds")
#     msg_late_task(port, 2000, MsgOne(n_servo=0, servo_pos=90))
#     print(f"{time.time() - t1} seconds")
#
#     return


def main(port: serial.Serial, debug: bool):
    print(INFO_TEXT["main"])

    # Arduino init
    print("Please wait...\n")
    send_msg(port, "Try start")
    time.sleep(4)
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
