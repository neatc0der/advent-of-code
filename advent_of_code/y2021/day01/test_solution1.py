#!/usr/bin/env python
from typing import Dict, List
from unittest import main, TestCase

from .solution1 import solve


class Tests2021_01_1(TestCase):
    def test_example(self) -> None:
        example_text: str = """
        199
        200
        208
        210
        200
        207
        240
        269
        260
        263
        """
        example_result: int = 7

        example: List[int] = list(
            int(line.strip())
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        result: Dict[str, int] = solve(example, key_inc="inc")
        self.assertEqual(result["inc"], example_result)

    def test_empty_contains_no_increase(self) -> None:
        result: Dict[str, int] = solve([], key_inc="inc")
        self.assertEqual(result["inc"], 0)

    def test_single_line_contains_no_increase(self) -> None:
        result: Dict[str, int] = solve([123], key_inc="inc")
        self.assertEqual(result["inc"], 0)

    def test_equal_lines_contain_no_increase(self) -> None:
        result: Dict[str, int] = solve([1, 1], key_inc="inc")
        self.assertEqual(result["inc"], 0)

    def test_decrease_lines_contain_no_increase(self) -> None:
        result: Dict[str, int] = solve([2, 1], key_inc="inc")
        self.assertEqual(result["inc"], 0)

    def test_increase_lines_contain_one_increase(self) -> None:
        result: Dict[str, int] = solve([1, 2], key_inc="inc")
        self.assertEqual(result["inc"], 1)

    def test_invalid_line_forces_exception(self) -> None:
        with self.assertRaises(RuntimeError):
            solve(["not a number"], key_inc="inc")


if __name__ == "__main__":
    main()

