import time

import serial

from config import *
from msg import MsgOne, MsgAll


def pack_msg(_msg):
    try:
        return str(_msg).encode('ascii')
    except Exception as e:
        raise TypeError(f"Incorrect type of {_msg} {type(_msg)}\n{e}")


def send_msg(ser: serial.Serial, msg):
    ser.write(pack_msg(msg))
    print(f"Sending message: {pack_msg(msg)}")
    # wait_msg(ser)


def wait_msg(ser: serial.Serial, limit=2000):
    line = ser.readline().decode('ascii')
    print(line)


def test1():
    time.sleep(5)
    send_msg(port, 'hello!')

    time.sleep(3)
    send_msg(port, MsgOne(0, 160))

    time.sleep(3)
    send_msg(port, MsgAll([60, 100, 80, 80]))


def main():
    text_to_print = 'привет мир'


if __name__ == '__main__':
    port = serial.Serial(PORT, SERIAL_SPEED)
    test1()
