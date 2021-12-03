from math import ceil, log2, pow
from typing import List, List

import attr


@attr.s
class PowerRate:
    gamma_bits: str = attr.ib(validator=attr.validators.matches_re(r"[01]+"))
    gamma: int = attr.ib(default=attr.Factory(
        lambda self: int(self.gamma_bits, base=2) if self.gamma_bits != "" else 0,
        takes_self=True,
    ))
    epsilon: int = attr.ib(default=attr.Factory(
        lambda self: int(pow(2, len(self.gamma_bits) or 1) - self.gamma - 1),
        takes_self=True,
    ))


def solve(lines: List[str]) -> PowerRate:
    assert isinstance(lines, list), "provided lines are not a list"
    assert len(lines) > 0, "provided lines is empty"
    bits: int = 0
    count: List[(int,) * bits] = []

    for line in lines:
        assert isinstance(line, str), f"invalid line input: '{line}'"

        if bits == 0:
            bits = len(line)
            count = [0] * bits
        
        assert len(line) == bits, f"exactly {bits} bits expected: '{line}'"

        for i in range(bits):
            assert line[i] in ("0", "1"), f"invalid line: '{line}'"

            if line[i] == "1":
                count[i] += 1

    gamma_bits: str = "".join(
        "1" if 2 * c >= len(lines) else "0"
        for c in count
    )

    return PowerRate(gamma_bits)
