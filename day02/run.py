#!/usr/bin/env python
import sys
from pathlib import Path
from typing import List

from solution1 import prepare as prepare1, solve as solve1, SubmarineCommand, SubmarinePosition
from solution2 import prepare as prepare2, solve as solve2, SubmarineAimCommand, SubmarineAimPosition


def main():
    path: Path = Path("input.txt")
    if not path.exists() or not path.is_file():
        print("argument is not a valid file path")
        sys.exit(2)

    with path.open() as fp:
        lines: List[str] = fp.readlines()

    try:
        commands1: List[SubmarineCommand] = prepare1(lines)
        commands2: List[SubmarineAimCommand] = prepare2(lines)

    except ValueError:
        print("invalid input: all lines must contain commands")
        sys.exit(3)

    position1: SubmarinePosition = solve1(commands1)
    position2: SubmarineAimPosition = solve2(commands2)    

    print("run: solve1 (Day 02, part 1)")
    print("->", position1.horizontal * position1.depth)

    print("run: solve1 (Day 02, part 2)")
    print("->", position2.horizontal * position2.depth)


if __name__ == "__main__":
    main()

