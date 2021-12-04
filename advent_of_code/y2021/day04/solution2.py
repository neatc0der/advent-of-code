from typing import Optional

import attr

from .solution1 import Board, Game as Game1


@attr.s
class Game(Game1):
    _last_winner: Optional[Board] = None

    def winning_board(self) -> Optional[Board]:
        winner: Optional[Board] = None
        for board in self.boards:
            if board.bingo:
                continue

            if winner is not None:
                return

            winner = board

        if winner is not None:
            self._last_winner = winner

        elif self._last_winner is not None:
            return self._last_winner
