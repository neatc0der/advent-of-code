from re import split
from typing import List, Optional, Set

import attr


@attr.s
class Board:
    matrix: List[List[int]] = attr.ib()
    marked: Set[int] = attr.ib(default=set())

    def mark(self, number: int) -> None:
        assert isinstance(number, int), f"not an integer: {number}"
        if any(number in row for row in self.matrix):
            self.marked.add(number)

    @property
    def unmarked(self):
        return set((n for row in self.matrix for n in row)) - self.marked

    @property
    def bingo(self) -> bool:
        matches: List[List[bool]] = [
            [
                number in self.marked
                for number in row
            ]
            for row in self.matrix
        ]
        
        row_match: bool = any(
            all(row)
            for row in matches
        )
        
        column_match: bool = any(
            all(
                row[i]
                for row in matches
            )
            for i in range(len(self.matrix))
        )

        return row_match or column_match

    @classmethod
    def create(cls, lines: List[str]) -> "Board":
        size: int = len(lines)
        matrix: List[List[int]] = []
        for line in lines:
            assert isinstance(line, str), f"invalid line input: '{line}'"
            line_split: List[str] = split('\s+', line.strip())
            assert len(line_split) == size, f"unexpected number of elements: '{line}'"
            assert all(i.isdigit() for i in line_split), f"not all elemnts are integer: '{line}'"
            numbers: List[int] = [int(n) for n in line_split]

            matrix.append(numbers)

        return cls(matrix)


@attr.s
class Score:
    marked: int = attr.ib()
    unmarked: int = attr.ib()


@attr.s
class Game:
    boards: List[Board] = attr.ib()
    marked: List[int] = attr.ib()

    @classmethod
    def create(cls, lines: List[str]) -> "Game":
        assert isinstance(lines, list), "provided lines are not a list"
        assert len(lines) > 2, "provided too few lines"

        marked_line: str = lines[0]
        line_split: List[str] = marked_line.strip().split(",")
        assert all(i.isdigit() for i in line_split), f"not all elemnts are integer: '{marked_line}'"
        marked: List[int] = [int(n) for n in line_split]

        index: int = 2
        assert isinstance(lines[index], str), f"invalid line input: '{lines[index]}'"

        size: int = len(lines[index].split())
        assert size > 1, f"too few elements per line: {size}"

        boards: List[Board] = []
        while index < len(lines):
            while index < len(lines) and lines[index] == "":
                index += 1
            assert index + size - 1 < len(lines), "insufficient lines for complete board"
            boards.append(Board.create(lines[index:index+size]))
            index += size
            
        return cls(boards, marked)

    def solve(self) -> Score:
        winner: Optional[Board] = None
        for marked in self.marked:
            for board in self.boards:
                board.mark(marked)

            winner = self.winning_board()
            if winner is not None:
                break

        assert winner is not None, "game cannot be won"
        return Score(
            marked=marked,
            unmarked=sum(winner.unmarked),
        )

    def winning_board(self) -> Optional[Board]:
        for board in self.boards:
            if board.bingo:
                return board
