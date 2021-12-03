#!/usr/bin/env python
from typing import List
from unittest import main, TestCase

from .solution1 import solve, PowerRate


class Tests2021_03_1(TestCase):
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

        example_result: int = 198

        example: List[str] = list(
            line.strip()
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        result: PowerRate = solve(example)
        self.assertEqual(result.epsilon * result.gamma, example_result)

    def test_rate_empty_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            PowerRate("")

    def test_rate_invalid_gamma_raises_error(self) -> None:
        with self.assertRaises(ValueError):
            PowerRate("abc")

    def test_gamma_represents_majority(self) -> None:
        result: PowerRate = solve([
            "00001111",
            "00110011",
            "01010101",
        ])
        self.assertEqual(result.gamma, int("00010111", base=2))
        self.assertEqual(result.epsilon, int("11101000", base=2))

    def test_gamma_if_equal_one_surpesses_zero(self) -> None:
        result: PowerRate = solve([
            "01",
            "10",
        ])
        self.assertEqual(result.gamma, int("11", base=2))
        self.assertEqual(result.epsilon, int("00", base=2))

    def test_rate_epsilon(self) -> None:
        gamma: str = "10110111"
        epsilon: str = "01001000"
        rate: PowerRate = PowerRate(gamma)

        self.assertEqual(f"{rate.gamma:08b}", gamma)
        self.assertEqual(f"{rate.epsilon:08b}", epsilon)

    def test_invalid_input_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            solve("hello")

    def test_invalid_data_type_of_line_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            solve([1])

    def test_invalid_line_content_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            solve(["abc"])

    def test_varying_bit_length_raises_error(self) -> None:
        with self.assertRaises(AssertionError):
            solve(["0", "11"])

    def test_identity(self) -> None:
        result: PowerRate = solve(["0101010"])
        self.assertEqual(result.gamma, int("0101010", base=2))
        self.assertEqual(result.epsilon, int("1010101", base=2))

    def test_no_lines_(self) -> None:
        with self.assertRaises(AssertionError):
            result: PowerRate = solve([])


if __name__ == "__main__":
    main()
