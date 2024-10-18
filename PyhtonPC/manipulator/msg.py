import dataclasses
from dataclasses import dataclass, field

from typing import Iterable, Iterator, List, Tuple, Union

from config import *


@dataclass
class MsgOne:
    msg_type: int = field(default=ord('O'), init=False)
    n_servo: int = field()
    servo_pos: int = field()

    def get(self):
        assert 0 <= self.n_servo < NUM_SERVOS
        assert 0 <= self.servo_pos < 180
        return [getattr(self, field.name) for field in dataclasses.fields(self)]


@dataclass
class MsgAll:
    msg_type: int = field(default=ord('A'), init=False)
    servo_pos: Iterable[int] = field(default_factory=list)

    def get(self):
        assert len(self.servo_pos) == NUM_SERVOS
        assert all((0 <= pos < 180 for pos in self.servo_pos))
        return [self.msg_type, *self.servo_pos]


if __name__ == '__main__':
    import struct

    # a = MsgOne(3, 4)
    a = MsgOne(2, 160)
    print(a.get())

    b = MsgAll([3, 4, 5, 6])
    print(b.get())

    r = struct.pack('b' * len(a.get()), *a.get())

    print(r)
