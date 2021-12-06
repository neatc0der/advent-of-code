from unittest import TestCase

from .solution import prepare, solve


class Tests06(TestCase):
    def test_example_80_days(self) -> None:
        example: str = "3,4,3,1,2"
        example_result: int = 5934

        result: int = solve(prepare(example), 80)
        self.assertEqual(result, example_result)

    def test_example_256_days(self) -> None:
        example: str = "3,4,3,1,2"
        example_result: int = 26984457539

        result: int = solve(prepare(example), 256)
        self.assertEqual(result, example_result)
