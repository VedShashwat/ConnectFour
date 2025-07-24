from __future__ import annotations
from dataclasses import dataclass, field
from enum import IntEnum
from typing import List, Optional

class Cell(IntEnum):
    EMPTY = 0
    P1 = 1
    P2 = 2

ROWS, COLS = 6, 7
FOUR = 4

@dataclass
class Board:
    grid: List[List[Cell]] = field(default_factory=lambda: [[Cell.EMPTY] * COLS for _ in range(ROWS)])

    def copy(self) -> "Board":
        return Board([row[:] for row in self.grid])

    def drop(self, col: int, player: Cell) -> bool:
        if not 0 <= col < COLS or self.grid[0][col] != Cell.EMPTY:
            return False
        for row in range(ROWS - 1, -1, -1):
            if self.grid[row][col] == Cell.EMPTY:
                self.grid[row][col] = player
                return True
        return False

    def legal_moves(self) -> List[int]:
        return [c for c in range(COLS) if self.grid[0][c] == Cell.EMPTY]

    def is_full(self) -> bool:
        return all(self.grid[0][c] != Cell.EMPTY for c in range(COLS))

    def winner(self) -> Optional[Cell]:
        lines = self._rows() + self._cols() + self._diagonals()
        for line in lines:
            for i in range(len(line) - FOUR + 1):
                window = line[i : i + FOUR]
                if window.count(window[0]) == FOUR and window[0] != Cell.EMPTY:
                    return Cell(window[0])
        return None

    def _rows(self):
        return self.grid

    def _cols(self):
        return [[self.grid[r][c] for r in range(ROWS)] for c in range(COLS)]

    def _diagonals(self):
        diags: List[List[Cell]] = []
        for r in range(ROWS):
            diags.append([self.grid[r + i][i] for i in range(min(ROWS - r, COLS))])
        for c in range(1, COLS):
            diags.append([self.grid[i][c + i] for i in range(min(ROWS, COLS - c))])
        for r in range(ROWS):
            diags.append([self.grid[r + i][COLS - 1 - i] for i in range(min(ROWS - r, COLS))])
        for c in range(COLS - 1):
            diags.append([self.grid[i][c - i] for i in range(min(ROWS, c + 1))])
        return diags

    def __str__(self) -> str:
        symbols = {Cell.EMPTY: ".", Cell.P1: "X", Cell.P2: "O"}
        rows = [" ".join(symbols[c] for c in row) for row in self.grid]
        return "\n".join(rows) + "\n" + " ".join(map(str, range(COLS)))
