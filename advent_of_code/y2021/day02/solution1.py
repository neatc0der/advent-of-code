from typing import Callable, Dict, List

import attr


@attr.s
class SubmarineCommand:
    horizontal: int = attr.ib(default=0)
    depth: int = attr.ib(default=0)


@attr.s
class SubmarinePosition(SubmarineCommand):
    def __add__(self, other: SubmarineCommand) -> "SubmarinePosition":
        assert isinstance(other, SubmarineCommand), "command is not a SubmarineCommand"
        return SubmarinePosition(
            horizontal=self.horizontal + other.horizontal,
            depth=self.depth + other.depth,
        )


def command_factory(line: str) -> List[SubmarineCommand]:
    assert isinstance(line, str), "input is not a string"
    split_line: List[str] = line.lower().split()
    assert len(split_line) == 2, f"invalid line: '{line}'"
    command: str = split_line[0]
    assert split_line[1].isdigit(), f"invalid parameter: '{split_line[1]}'"
    value: int = int(split_line[1])

    command_map: Dict[str, Callable[[str], SubmarineCommand]] = {
        "forward": lambda v: SubmarineCommand(horizontal=v),
        "up": lambda v: SubmarineCommand(depth=-v),
        "down": lambda v: SubmarineCommand(depth=v),
    }

    assert command in command_map, f"invalid command: '{command}'"
    return command_map[command](value)

def prepare(lines: List[str]) -> List[SubmarineCommand]:
    assert isinstance(lines, list), "lines are not a list"
    return list(command_factory(line) for line in lines)


def solve(commands: List[SubmarineCommand]) -> SubmarinePosition:
    assert isinstance(commands, list), "commands are not a list"
    position: SubmarinePosition = SubmarinePosition()
    
    for command in commands:
        assert isinstance(command, SubmarineCommand), "command is not a SubmarineCommand"
        position += command

    return position
