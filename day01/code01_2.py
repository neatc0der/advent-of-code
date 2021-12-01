#!/usr/bin/env python
import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional

from code01_1 import solve as solve01_1


def prepare(lines: List[int]) -> List[int]:
    if not isinstance(lines, List):
        raise RuntimeError("invalid input: no list provided")

    new_numbers: List[int] = []

    window: int = 0
    windows: List[Optional[int]] = [None] * 3
    for i, number in enumerate(lines):
        if not isinstance(number, int):
            raise RuntimeError(f"invalid input in line {i}: '{number}' (not an int)")

        for w in range(len(windows)):
            if windows[w] is None and w != window:
                continue

            if w == window:
                windows[w] = number

            else:
                windows[w] += number

        window = (window + 1) % len(windows)

        if windows[window] is not None:
            new_numbers.append(windows[window])

    return new_numbers



def solve(lines: List[int], **kwargs) -> Dict[str, int]:
    new_lines: List[int] = prepare(lines)
    return solve01_1(new_lines, **kwargs)

