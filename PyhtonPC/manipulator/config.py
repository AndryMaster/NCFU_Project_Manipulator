from utils import *

DEBUG = True

# Arduino
NUM_SERVOS = 4

# Serial
PORT = 'COM5'
SERIAL_SPEED = 115200

# Control
CYCLE_TIME = 100e-3
IS_CONTROL = False
CUR_POS = [90] * 4
ADD_POS = [1] * 4
MUL_POS = {'key': 'shift',
           'mul': 10}
CONTROL = {
    # 0: {'keys': 'up down'.split(),
    #     'ctrl_pos': True, },
    # 1: {'keys': 'up down'.split(),
    #     'ctrl_pos': False, },
    # 2: {'keys': 'left right'.split(),
    #     'ctrl_pos': False, },
    # 3: {'keys': 'left right'.split(),
    #     'ctrl_pos': True, },
    0: 'w s'.split(),
    1: 'up down'.split(),
    2: 'left right'.split(),
    3: 'a d'.split(),
}
