from utils import *

DEBUG = True

# Arduino
NUM_SERVOS = 4

# Serial
PORT = 'COM5'
SERIAL_SPEED = 115200  # 115200 9600

# Control
CYCLE_TIME = 100e-3
IS_CONTROL = False
IS_CHANGED = False
CUR_POS = [90] * 4
# ADD_POS = [2] * 4
# MUL_POS = {'key': 'shift',
#            'mul': 5}
MULTY_ADD_POS = {
    'shift': [1]  * NUM_SERVOS,
    'alt':   [5]  * NUM_SERVOS,
    'else':  [10] * NUM_SERVOS,
}
CONTROL = {
    0: {'keys': 'w s'.split(),
        'ctrl_pos': False, },
    1: {'keys': 'left right'.split(),
        'ctrl_pos': False, },
    2: {'keys': 'up down'.split(),
        'ctrl_pos': False, },
    3: {'keys': 'a d'.split(),
        'ctrl_pos': False, },
    # 0: 'w s'.split(),
    # 1: 'up down'.split(),
    # 2: 'left right'.split(),
    # 3: 'a d'.split(),
}
