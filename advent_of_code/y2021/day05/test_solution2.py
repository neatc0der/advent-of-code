from typing import List
from unittest import TestCase

from .solution2 import Solver


class Tests05_2(TestCase):
    def test_example(self) -> None:
        example_text: str = """
        0,9 -> 5,9
        8,0 -> 0,8
        9,4 -> 3,4
        2,2 -> 2,1
        7,0 -> 7,4
        6,4 -> 2,0
        0,9 -> 2,9
        3,4 -> 1,4
        0,0 -> 8,8
        5,5 -> 8,2
        """

        example_result: int = 12

        example: List[str] = list(
            line.strip()
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        solver: Solver = Solver.create(example)
        result: int = solver.solve()

        self.assertEqual(result, example_result)
