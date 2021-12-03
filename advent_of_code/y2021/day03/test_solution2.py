#!/usr/bin/env python
from typing import List
from unittest import main, TestCase

from .solution2 import solve, AirRate


class Tests2021_03_2(TestCase):
    def test_example(self) -> None:
        example_text: str = """
        00100
        11110
        10110
        10111
        10101
        01111
        00111
        11100
        10000
        11001
        00010
        01010
        """

        example_result: int = 230

        example: List[str] = list(
            line.strip()
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        result: AirRate = solve(example)
        self.assertEqual(result.generator * result.scrubber, example_result)


if __name__ == "__main__":
    main()
