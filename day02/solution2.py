from typing import List

import attr


@attr.s
class SubmarineAimCommand:
    horizontal: int = attr.ib(default=0)
    aim: int = attr.ib(default=0)

@attr.s
class SubmarineAimPosition(SubmarineAimCommand):
    depth: int = attr.ib(default=0)

    def __add__(self, other: SubmarineAimCommand) -> "SubmarineAimPosition":
        aim: int = self.aim + other.aim
        return SubmarineAimPosition(
            horizontal=self.horizontal + other.horizontal,
            aim=aim,
            depth=self.depth + aim * other.horizontal,
        )


def command_factory(line: str) -> List[SubmarineAimCommand]:
    try:
        command, value = line.lower().split()
    except ValueError:
        raise RuntimeError(f"invalid line: '{line}'")

    try:
        value = int(value)
    except ValueError:
        raise RuntimeError(f"invalid parameter: '{value}'")

    if command == "forward":
        return SubmarineAimCommand(horizontal=value)
    if command == "up":
        return SubmarineAimCommand(aim=-value)
    if command == "down":
        return SubmarineAimCommand(aim=value)
    
    raise RuntimeError(f"invalid command: '{command}'")


def prepare(lines: List[str]) -> List[SubmarineAimCommand]:
    return list(command_factory(line) for line in lines)


def solve(commands: List[SubmarineAimCommand]) -> SubmarineAimPosition:
    position: SubmarineAimPosition = SubmarineAimPosition()
    
    for command in commands:
        position += command

    return position

