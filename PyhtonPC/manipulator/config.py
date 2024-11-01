DEBUG = False

# Arduino
NUM_SERVOS = 4

# Serial
PORT = 'COM5'
SERIAL_SPEED = 115200  # 115200 9600

# Control
SEND_DELAY = 0.07
LAST_SEND = None
CUR_POS = [90] * 4
MULTY_ADD_POS = {
    'shift':   [1]  * NUM_SERVOS,
    'ctrl':    [5]  * NUM_SERVOS,
    'alt':     [20] * NUM_SERVOS,
    'default': [10] * NUM_SERVOS,
}
CONTROL = {
    0: {'keys': 's w'.split(),},
    1: {'keys': 'right left'.split(),},
    2: {'keys': 'up down'.split(),},
    3: {'keys': 'a d'.split(),},
}
ALL_CONTROL_KEYS = set([sub_val for val in CONTROL.values() for sub_val in val['keys']])

INFO_TEXT = {
    "main": """Select control`s mode:
\t1) Command line mode (CLI)
\t2) Keyboard control (wasd)
\t3) Print text mode\n""",

    "mode_cli": """ModeINFO:
Using message format like: "A 120 90 50 80", "O 0 120" and other.
Read <MessageType.md> file for more info\n""",

    "mode_control": """ModeINFO:
Using (w, a, s, d, up, down, left, right) keys to moving.
Modifiers (speed in degrees): <shift>=1 <alt>=5 default=10
<Enter> to get my position\n""",

    "mode_print_text": """ModeINFO:
qwerty\n""",
}
