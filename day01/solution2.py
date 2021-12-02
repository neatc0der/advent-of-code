#!/usr/bin/env python
from typing import Dict, List, Optional

from solution1 import solve as solve1


def prepare(lines: List[int]) -> List[int]:
    if not isinstance(lines, List):
        raise RuntimeError("invalid input: no list provided")

    new_numbers: List[int] = []

    window_size: int = 3
    window: int = 0
    windows: List[Optional[int]] = [None] * window_size
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

        window = (window + 1) % window_size

        if windows[window] is not None:
            new_numbers.append(windows[window])

    return new_numbers



def solve(lines: List[int], **kwargs) -> Dict[str, int]:
    new_lines: List[int] = prepare(lines)
    return solve1(new_lines, **kwargs)

