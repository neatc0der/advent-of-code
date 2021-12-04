#!/usr/bin/env python
import os
import sys
from pathlib import Path
from typing import List

from .solution1 import Game as Game1, Score
from .solution2 import Game as Game2


def main():
    path: Path = Path(os.path.dirname(__file__), "input.txt")
    if not path.exists() or not path.is_file():
        print("argument is not a valid file path")
        sys.exit(2)

    with path.open() as fp:
        lines: List[str] = list(line.strip() for line in fp.readlines())

    score1: Score = Game1.create(lines).solve()
    score2: Score = Game2.create(lines).solve()

    print("run: solve1 (Day 04, part 1)")
    print("->", score1.marked * score1.unmarked)

    print("run: solve2 (Day 04, part 2)")
    print("->", score2.marked * score2.unmarked)


if __name__ == "__main__":
    main()
