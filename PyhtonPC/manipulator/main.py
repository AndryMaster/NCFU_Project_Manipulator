import time
import serial
import keyboard

from config import *
from msg import *
# from control import set_actual, get_current_position


def pack_msg(_msg):
    try:
        return str(_msg).encode('ascii')
    except Exception as e:
        raise TypeError(f"Incorrect type of {_msg} {type(_msg)}\n{e}")


def send_msg(port: serial.Serial, msg, debug=False):
    port.write(pack_msg(msg))
    if debug:
        print(f"Sending message: {pack_msg(msg)}")


def get_msg_all(port: serial.Serial, debug=False):
    if port.in_waiting > 0:
        text = port.read(port.in_waiting).decode('cp1251')  # .decode('ascii')
        if debug:
            print(f"Out>: {text.strip()}")
        return text
    # while port.in_waiting > 0:
    #     try:
    #         line = port.readline().decode('ascii')
    #         print(line)
    #     except Exception as e:
    #         pass
    # return line


# def test1():
#     time.sleep(5)
#     send_msg(port, 'hello!')
#     time.sleep(3)
#     send_msg(port, MsgOne(0, 160))
#     time.sleep(3)
#     send_msg(port, MsgAll([60, 100, 80, 80]))


def set_actual(event: keyboard.KeyboardEvent):
    global IS_CONTROL, CUR_POS, port
    IS_CONTROL = not IS_CONTROL
    if IS_CONTROL:
        CUR_POS = [90] * 4
        print(f'Control ON ({CUR_POS})')
        send_msg(port, MsgAll(CUR_POS))
    else:
        print('Control OFF')


def get_current_position(event: keyboard.KeyboardEvent):
    print(CUR_POS)


def control_with_keys(event: keyboard.KeyboardEvent):
    print(CUR_POS)


def main(port: serial.Serial):
    print(f"Control speed: {[e / CYCLE_TIME for e in ADD_POS]} deg/sec")
    keyboard.on_press_key('f2', set_actual)
    keyboard.on_press_key('enter', get_current_position)

    # keyboard.on_release_key('up')

    while True:
        if keyboard.is_pressed('esc'):
            break

        get_msg_all(port)

        # Control
        if IS_CONTROL:
            is_change = False

            for key, val in CONTROL.items():
                val_pressed = [keyboard.is_pressed(v) for v in val]
                if val_pressed[0] and not val_pressed[1]:
                    CUR_POS[key] = clip(CUR_POS[key] + ADD_POS[key])
                    is_change = True
                elif not val_pressed[0] and val_pressed[1]:
                    CUR_POS[key] = clip(CUR_POS[key] - ADD_POS[key])
                    is_change = True

            # if is_change:
            send_msg(port, MsgAll(CUR_POS))

            # time.sleep(CYCLE_TIME)

        else:
            line = input("Command in<: ")
            send_msg(port, line)


if __name__ == '__main__':
    DEBUG = False
    port = serial.Serial(PORT, SERIAL_SPEED)
    # test1()
    main(port)
