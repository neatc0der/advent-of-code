from typing import Callable, List

from .solution1 import solve as solve1, PowerRate

import attr


@attr.s
class AirRate:
    generator: int = attr.ib()
    scrubber: int = attr.ib()


def partial_solve(lines: List[str], compare: Callable[[str, str], bool]) -> int:
    reduced_list: List[str] = list(lines)
    bit: int = 0

    while len(reduced_list) > 1:
        rate: PowerRate = solve1(reduced_list)

        reduced_list = list(filter(lambda l: compare(l[bit], rate.gamma_bits[bit]), reduced_list))

        bit += 1
        if bit > len(rate.gamma_bits):
            break
    
    return int(reduced_list[0], base=2)


def solve(lines: List[str]) -> AirRate:
    return AirRate(
        generator=partial_solve(lines, lambda x, y: x == y),
        scrubber=partial_solve(lines, lambda x, y: x != y),
    )
