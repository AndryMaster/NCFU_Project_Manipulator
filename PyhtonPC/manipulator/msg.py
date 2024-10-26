import serial
from dataclasses import dataclass, field
from typing import Iterable, Iterator, List, Tuple, Union

from config import *


class MsgTypes:
    MSG_ONE = 'O'
    MSG_ALL = 'A'
    MSG_KEY_PRESS = 'K'
    MSG_TEXT = 'T'
    MSG_GET_POS = 'G'


@dataclass
class MsgOne:
    # msg_type: int = field(default=ord('O'), init=False)
    n_servo: int
    servo_pos: int

    def __str__(self):
        assert 0 <= self.n_servo < NUM_SERVOS
        assert 0 <= self.servo_pos <= 180
        return f"{MsgTypes.MSG_ONE} {self.n_servo} {self.servo_pos}"


@dataclass
class MsgAll:
    # msg_type: int = field(default=ord('A'), init=False)
    many_servo_pos: List[int]

    def __str__(self):
        assert len(self.many_servo_pos) == NUM_SERVOS
        assert all((0 <= pos <= 180 for pos in self.many_servo_pos))
        return f"{MsgTypes.MSG_ALL} {' '.join(map(str, self.many_servo_pos))}"


@dataclass
class MsgKeyPress:
    key_button: str
    many_servo_pos: List[int]

    def __str__(self):
        assert len(self.key_button) == 1
        assert len(self.many_servo_pos) == NUM_SERVOS
        assert all((0 <= pos < 180 for pos in self.many_servo_pos))
        return f"{MsgTypes.MSG_KEY_PRESS} {' '.join(map(str, self.many_servo_pos))} {self.key_button}"


@dataclass
class MsgText:
    text: str

    def __str__(self):
        assert len(self.text) < 64
        return f"{MsgTypes.MSG_TEXT} {self.text}"


@dataclass
class MsgGetPos:
    def __str__(self):
        return "G"


if __name__ == '__main__':  # Test
    a = MsgOne(2, 160)
    print(a)

    b = MsgAll([90, 120, 40, 160])
    print(b)

    c = MsgKeyPress('ы', [90, 120, 40, 160])
    print(c)

    d = MsgText('Hello world!')
    print(d)

    e = MsgGetPos()
    print(e)
