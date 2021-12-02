from typing import List

import attr


@attr.s
class SubmarineCommand:
    horizontal: int = attr.ib(default=0)
    depth: int = attr.ib(default=0)


@attr.s
class SubmarinePosition(SubmarineCommand):
    def __add__(self, other: SubmarineCommand) -> "SubmarinePosition":
        return SubmarinePosition(
            horizontal=self.horizontal + other.horizontal,
            depth=self.depth + other.depth,
        )


def command_factory(line: str) -> List[SubmarineCommand]:
    try:
        command, value = line.lower().split()
    except ValueError:
        raise RuntimeError(f"invalid line: '{line}'")

    try:
        value = int(value)
    except ValueError:
        raise RuntimeError(f"invalid parameter: '{value}'")

    if command == "forward":
        return SubmarineCommand(horizontal=value)
    if command == "up":
        return SubmarineCommand(depth=-value)
    if command == "down":
        return SubmarineCommand(depth=value)
    
    raise RuntimeError(f"invalid command: '{command}'")


def prepare(lines: List[str]) -> List[SubmarineCommand]:
    return list(command_factory(line) for line in lines)


def solve(commands: List[SubmarineCommand]) -> SubmarinePosition:
    position: SubmarinePosition = SubmarinePosition()
    
    for command in commands:
        position += command

    return position
