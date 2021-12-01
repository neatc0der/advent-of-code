#!/usr/bin/env python
import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional

from code01_1 import solve as solve01_1
from code01_2 import solve as solve01_2

def main():
    path: Path = Path("input.txt")
    if not path.exists() or not path.is_file():
        print("argument is not a valid file path")
        sys.exit(2)

    with path.open() as fp:
        lines: List[str] = fp.readlines()

    try:
        numbers = list(
            int(line)
            for line in lines
        )
    except ValueError:
        print("invalid input: all lines must contain integers")
        sys.exit(3)

    print("run: solve01_1")
    print(solve01_1(numbers))

    print("run: solve01_2")
    print(solve01_2(numbers))


if __name__ == "__main__":
    main()

