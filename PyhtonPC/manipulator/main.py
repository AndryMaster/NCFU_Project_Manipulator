import time
from argparse import ArgumentTypeError

import serial
import struct

from config import *
from msg import MsgOne, MsgAll


def get_struct_pack(fresh_msg):
    if hasattr(fresh_msg, "get"):  # callable(getattr(args[0], "get")):
        return struct.pack('b' * len(fresh_msg.get()), *fresh_msg.get())
    elif isinstance(fresh_msg, str):
        return fresh_msg.encode('ascii')
    raise ArgumentTypeError(fresh_msg)


def send_msg(ser: serial.Serial, msg):
    ser.write(get_struct_pack(msg))
    wait_msg(ser)


def wait_msg(ser: serial.Serial, limit=2000):
    line = ser.readline().decode('ascii')
    print(line)


port = serial.Serial(PORT, SERIAL_SPEED)


send_msg(port, 'hello!')

time.sleep(3)

send_msg(port, MsgOne(0, 160))

# print("waiting for arduino...")
# line = b""
# while not b"READY" in line:
#     line = port.readline().decode('ascii')
