#!/usr/bin/env python
import os
import sys
from pathlib import Path
from typing import List

from .solution1 import Solver as Solver1
from .solution2 import Solver as Solver2


def main():
    path: Path = Path(os.path.dirname(__file__), "input.txt")
    if not path.exists() or not path.is_file():
        print("argument is not a valid file path")
        sys.exit(2)

    with path.open() as fp:
        lines: List[str] = list(line.strip() for line in fp.readlines())

    result1: int = Solver1.create(lines).solve()
    result2: int = Solver2.create(lines).solve()

    print("run: solve1 (Day 05, part 1)")
    print("->", result1)

    print("run: solve2 (Day 05, part 2)")
    print("->", result2)


if __name__ == "__main__":
    main()
