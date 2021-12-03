from typing import Callable, Dict, List

import attr


@attr.s
class SubmarineAimCommand:
    horizontal: int = attr.ib(default=0)
    aim: int = attr.ib(default=0)

@attr.s
class SubmarineAimPosition(SubmarineAimCommand):
    depth: int = attr.ib(default=0)

    def __add__(self, other: SubmarineAimCommand) -> "SubmarineAimPosition":
        assert isinstance(other, SubmarineAimCommand), "command is not a SubmarineAimCommand"
        aim: int = self.aim + other.aim
        return SubmarineAimPosition(
            horizontal=self.horizontal + other.horizontal,
            aim=aim,
            depth=self.depth + aim * other.horizontal,
        )


def command_factory(line: str) -> List[SubmarineAimCommand]:
    assert isinstance(line, str), "input is not a string"
    split_line: List[str] = line.lower().split()
    assert len(split_line) == 2, f"invalid line: '{line}'"
    command: str = split_line[0]
    assert split_line[1].isdigit(), f"invalid parameter: '{split_line[1]}'"
    value: int = int(split_line[1])

    command_map: Dict[str, Callable[[str], SubmarineAimCommand]] = {
        "forward": lambda v: SubmarineAimCommand(horizontal=v),
        "up": lambda v: SubmarineAimCommand(aim=-v),
        "down": lambda v: SubmarineAimCommand(aim=v),
    }

    assert command in command_map, f"invalid command: '{command}'"
    return command_map[command](value)


def prepare(lines: List[str]) -> List[SubmarineAimCommand]:
    assert isinstance(lines, list), "lines are not a list"
    return list(command_factory(line) for line in lines)


def solve(commands: List[SubmarineAimCommand]) -> SubmarineAimPosition:
    assert isinstance(commands, list), "commands are not a list"
    position: SubmarineAimPosition = SubmarineAimPosition()
    
    for command in commands:
        assert isinstance(command, SubmarineAimCommand), "command is not a SubmarineAimCommand"
        position += command

    return position

