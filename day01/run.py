#!/usr/bin/env python
import sys
from pathlib import Path
from typing import List

from solution1 import solve as solve1
from solution2 import solve as solve2


def main():
    path: Path = Path("input.txt")
    if not path.exists() or not path.is_file():
        print("argument is not a valid file path")
        sys.exit(2)

    with path.open() as fp:
        lines: List[str] = fp.readlines()

    try:
        numbers: List[int] = list(
            int(line)
            for line in lines
        )
    except ValueError:
        print("invalid input: all lines must contain integers")
        sys.exit(3)

    print("run: solve1 (Day 01, part 1)")
    print("->", solve1(numbers, key_inc="inc")["inc"])

    print("run: solve2 (Day 01, part 2)")
    print("->", solve2(numbers, key_inc="inc")["inc"])


if __name__ == "__main__":
    main()

