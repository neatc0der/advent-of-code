from typing import List
from unittest import TestCase

from .solution1 import Point, PointRange, Solver


class Tests05_1(TestCase):
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

        example_result: int = 5

        example: List[str] = list(
            line.strip()
            for line in example_text.split("\n")
            if line.strip() != ""
        )

        solver: Solver = Solver.create(example)
        result: int = solver.solve()

        self.assertEqual(result, example_result)

    def test_point_create(self) -> None:
        point: Point = Point.create("1,2")
        self.assertEqual(point, Point(1, 2))

    def test_point_range_create(self) -> None:
        point_range: PointRange = PointRange.create("1,2 -> 1,4")
        self.assertEqual(point_range.start, Point(1, 2))
        self.assertEqual(point_range.end, Point(1, 4))
        self.assertEqual(list(point_range.points), [Point(1, 2), Point(1, 3), Point(1, 4)])
