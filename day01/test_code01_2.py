#!/usr/bin/env python
from unittest import main, TestCase

from code01_2 import prepare, solve


class Tests01_2(TestCase):
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

        example: List[int] = list(
            int(line.strip())
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        example_result: List[int] = [
            607,
            618,
            618,
            617,
            647,
            716,
            769,
            792,
        ]

        prepare_result: List[int] = prepare(example)

        self.assertEqual(prepare_result, example_result)
        self.assertEqual(solve(example, key_inc="inc")["inc"], 5)

    def test_empty_lines_have_empty_result(self) -> None:
        self.assertEqual(prepare([]), [])

    def test_single_line_has_empty_result(self) -> None:
        self.assertEqual(prepare([1]), [])

    def test_two_lines_have_empty_result(self) -> None:
        self.assertEqual(prepare([1, 2]), [])

    def test_three_lines_have_one_result(self) -> None:
        self.assertEqual(prepare([1, 2, 3]), [6])

    def test_four_lines_have_two_result(self) -> None:
        self.assertEqual(prepare([1, 2, 3, 4]), [6, 9])


if __name__ == "__main__":
    main()

