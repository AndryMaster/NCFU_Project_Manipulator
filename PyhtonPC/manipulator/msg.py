import dataclasses
from dataclasses import dataclass


@dataclass
class MsgOne:
    n_servo: int
    servo_pos: int

    def get(self):
        return [getattr(self, field.name) for field in dataclasses.fields(self)]
