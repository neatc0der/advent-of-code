from typing import Dict, List


def prepare(line: str) -> List[int]:
    assert isinstance(line, str)
    assert len(line) > 0

    line_split: List[str] = line.split(",")
    assert all(n.isdigit() for n in line_split)

    return [int(n) for n in line_split]


def solve(fish_list: List[int], days: int) -> int:
    assert isinstance(fish_list, list)
    assert all(isinstance(f, int) for f in fish_list)
    assert all(0 <= f <= 8 for f in fish_list)

    lanternfish: Dict[int, int] = {
        i: sum(1 if f == i else 0 for f in fish_list)
        for i in range(9)
    }

    for _ in range(days):
        lanternfish = day(lanternfish)

    return sum(lanternfish.values())


def day(lanternfish: Dict[int, int]) -> Dict[int, int]:
    new_fish: int = lanternfish[0]
    for i in range(1, 9):
        lanternfish[i - 1] = lanternfish[i]

    lanternfish[6] += new_fish
    lanternfish[8] = new_fish

    return lanternfish
