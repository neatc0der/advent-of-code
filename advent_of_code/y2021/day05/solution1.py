from copy import copy
from typing import Generator, List

import attr


@attr.s
class Point:
    x: int = attr.ib()
    y: int = attr.ib()

    @classmethod
    def create(cls, point: str) -> "Point":
        assert isinstance(point, str), f"point not a string: '{point}'"
        assert len(point) > 2, f"insufficient content for point: '{point}'"
        coordinates: List[str] = point.split(",")
        assert len(coordinates) == 2, f"exactly 2 coodinates required: '{point}'"
        assert coordinates[0].isdigit(), f"first coordinate not a number: '{coordinates[0]}'"
        assert coordinates[1].isdigit(), f"first coordinate not a number: '{coordinates[1]}'"
        
        return cls(
            x=int(coordinates[0]),
            y=int(coordinates[1]),
        )


@attr.s
class PointRange:
    start: Point = attr.ib()
    end: Point = attr.ib()
    ignore_diagonale: bool = attr.ib(default=True)

    @property
    def points(self) -> Generator[Point, None, None]:
        if self.ignore_diagonale and self.start.x != self.end.x and self.start.y != self.end.y:
            return

        point: Point = copy(self.start)
        while point != self.end:
            yield copy(point)

            if point.x != self.end.x:
                point.x += 1 if point.x < self.end.x else -1

            if point.y != self.end.y:
                point.y += 1 if point.y < self.end.y else -1

        yield copy(self.end)

    @classmethod
    def create(cls, point_range: str, ignore_diagonale: bool = True) -> "PointRange":
        assert isinstance(point_range, str), f"point range not a string: '{point_range}'"
        assert len(point_range) > 7, f"insufficient content for point range: '{point_range}'"
        points: List[str] = point_range.split("->")
        assert len(points) == 2, f"exactly 2 points required: '{point_range}'"

        return cls(
            start=Point.create(points[0].strip()),
            end=Point.create(points[1].strip()),
            ignore_diagonale=ignore_diagonale,
        )


@attr.s
class Solver:
    ignore_diagonale: bool = True

    ranges: List[PointRange] = attr.ib()

    @classmethod
    def create(cls, lines: List[str]) -> "Solver":
        assert isinstance(lines, list), "provided lines are not a list"
        assert len(lines) > 1, "provided too few lines"
        return Solver(ranges=[
            PointRange.create(line, cls.ignore_diagonale)
            for line in lines
        ])

    def solve(self) -> int:
        max_x: int = max(p.x for pr in self.ranges for p in (pr.start, pr.end)) + 1
        max_y: int = max(p.y for pr in self.ranges for p in (pr.start, pr.end)) + 1

        diagram: List[List[int]] = [
            [0] * max_x
            for i in range(max_y)
        ]
        for point_range in self.ranges:
            for point in point_range.points:
                diagram[point.x][point.y] += 1

        return sum(
            1 if count >= 2 else 0
            for row in diagram
            for count in row
        )
