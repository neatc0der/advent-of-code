#!/usr/bin/env python
import os
import sys
from pathlib import Path
from typing import List

from .solution1 import solve as solve1, PowerRate
from .solution2 import solve as solve2, AirRate


def main():
    path: Path = Path(os.path.dirname(__file__), "input.txt")
    if not path.exists() or not path.is_file():
        print("argument is not a valid file path")
        sys.exit(2)

    with path.open() as fp:
        lines: List[str] = list(line.strip() for line in fp.readlines())

    rate1: PowerRate = solve1(lines)
    rate2: AirRate = solve2(lines)

    print("run: solve1 (Day 03, part 1)")
    print("->", rate1.gamma * rate1.epsilon)

    print("run: solve2 (Day 03, part 2)")
    print("->", rate2.generator * rate2.scrubber)


if __name__ == "__main__":
    main()
