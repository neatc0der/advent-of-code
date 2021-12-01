#!/usr/bin/env python
import sys
from pathlib import Path
from typing import Callable, Dict, List, Optional


def solve(lines: List[int], key_inc: str = "increased", key_dec: str = "decreased", key_eq: str = "equal") -> Dict[str, int]:
    if not isinstance(lines, List):
        raise RuntimeError("invalid input: no list provided")

    mapping: Dict[str, Callable[[int, int], bool]] = {
        key_inc: lambda x, y: x > y,
        key_dec: lambda x, y: x < y,
        key_eq: lambda x, y: x == y,
    }

    count: Dict[str, int] = {
        key_inc: 0,
        key_dec: 0,
        key_eq: 0,
    }
    prev_number: Optional[int] = None
    for i, number in enumerate(lines):
        if not isinstance(number, int):
            raise RuntimeError(f"invalid input in line {i}: '{number}' (not an int)")

        if prev_number is not None:
            for key, validator in mapping.items():
                if validator(number, prev_number):
                    count[key] += 1
                    break

        prev_number = number

    return count

