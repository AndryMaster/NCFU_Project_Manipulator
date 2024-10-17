import serial
import struct


def get_struct_pack(*args):
    return struct.pack('b' * len(args), *args)


# port = serial.Serial('COM5', 9600)
#
# print("waiting for arduino...")
# line = b""
# while not b"READY" in line:
#     line = port.readline().decode('ascii')

