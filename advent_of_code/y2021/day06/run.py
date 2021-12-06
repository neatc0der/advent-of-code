#!/usr/bin/env python
import os
import sys
from pathlib import Path
from typing import List

from .solution import prepare, solve


def main():
    path: Path = Path(os.path.dirname(__file__), "input.txt")
    if not path.exists() or not path.is_file():
        print("argument is not a valid file path")
        sys.exit(2)

    with path.open() as fp:
        lines: List[str] = list(line.strip() for line in fp.readlines())

    line: str = lines[0]

    result1: int = solve(prepare(line), 80)
    result2: int = solve(prepare(line), 256)

    print("run: solve1 (Day 06, part 1)")
    print("->", result1)

    print("run: solve2 (Day 06, part 2)")
    print("->", result2)


if __name__ == "__main__":
    main()
