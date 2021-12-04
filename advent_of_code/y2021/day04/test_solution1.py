#!/usr/bin/env python
from typing import List
from unittest import main, TestCase

from .solution1 import Board, Game, Score


class Tests04_1(TestCase):
    def test_example(self) -> None:
        example_text: str = """
        7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

        22 13 17 11  0
        8  2 23  4 24
        21  9 14 16  7
        6 10  3 18  5
        1 12 20 15 19

        3 15  0  2 22
        9 18 13 17  5
        19  8  7 25 23
        20 11 10 24  4
        14 21 16 12  6

        14 21 17 24  4
        10 16 15  9 19
        18  8 23 26 20
        22 11 13  6  5
        2  0 12  3  7
        """

        example_result: int = 4512

        example: List[str] = example_text.split("\n")[1:-1]

        game: Game = Game.create(example)
        result: Score = game.solve()

        self.assertEqual(result.marked * result.unmarked, example_result)

    def test_board_create(self) -> None:
        board: Board = Board.create([
            " 1  2  3  4  5",
            " 6  7  8  9 10",
            "11 12 13 14 15",
            "16 17 18 19 20",
            "21 22 23 24 25",
        ])

        self.assertEqual(board, Board([
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25],
        ]))

    def test_board_no_bingo(self) -> None:
        board: Board = Board(
            matrix = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            marked={1, 7, 13, 19, 25},
        )

        self.assertFalse(board.bingo)

    def test_board_bingo_on_row(self) -> None:
        board: Board = Board(
            matrix = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            marked={1, 2, 3, 4, 5},
        )

        self.assertTrue(board.bingo)

    def test_board_bingo_on_column(self) -> None:
        board: Board = Board(
            matrix = [
                [1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25],
            ],
            marked={1, 6, 11, 16, 21},
        )

        self.assertTrue(board.bingo)


if __name__ == "__main__":
    main()
