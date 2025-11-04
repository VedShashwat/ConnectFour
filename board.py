from typing import List, Optional
from enum import Enum
from copy import deepcopy

ROWS = 6
COLS = 7
FOUR = 4


class Cell(Enum):
    """Represents a cell on the board."""
    EMPTY = 0
    P1 = 1
    P2 = 2


class Board:
    """Represents a Connect Four game board."""
    
    def __init__(self):
        """Initialize an empty board."""
        self.grid: List[List[Cell]] = [[Cell.EMPTY for _ in range(COLS)] for _ in range(ROWS)]
    
    def __str__(self) -> str:
        """Return a string representation of the board."""
        symbols = {Cell.EMPTY: ".", Cell.P1: "X", Cell.P2: "O"}
        lines = []
        lines.append("  " + " ".join(str(i) for i in range(COLS)))
        lines.append("  " + "-" * (COLS * 2 - 1))
        for row in self.grid:
            lines.append("  " + " ".join(symbols[cell] for cell in row))
        return "\n".join(lines)
    
    def drop(self, col: int, player: Cell) -> bool:
        """
        Drop a piece into the specified column.
        
        Args:
            col: Column index (0 to COLS-1)
            player: The player making the move
            
        Returns:
            True if the move was successful, False otherwise
        """
        if col < 0 or col >= COLS:
            return False
        
        # Find the lowest empty row in this column
        for row in range(ROWS - 1, -1, -1):
            if self.grid[row][col] == Cell.EMPTY:
                self.grid[row][col] = player
                return True
        
        return False  # Column is full
    
    def legal_moves(self) -> List[int]:
        """Return a list of columns where a piece can be dropped."""
        moves = []
        for col in range(COLS):
            if self.grid[0][col] == Cell.EMPTY:
                moves.append(col)
        return moves
    
    def is_full(self) -> bool:
        """Check if the board is completely full."""
        return len(self.legal_moves()) == 0
    
    def winner(self) -> Optional[Cell]:
        """
        Check if there's a winner.
        
        Returns:
            The winning player (Cell.P1 or Cell.P2) or None if no winner
        """
        # Check all possible lines
        for line in self._rows() + self._cols() + self._diagonals():
            winner = self._check_line(line)
            if winner:
                return winner
        return None
    
    def copy(self) -> 'Board':
        """Create a deep copy of the board."""
        new_board = Board()
        new_board.grid = deepcopy(self.grid)
        return new_board
    
    def _rows(self) -> List[List[Cell]]:
        """Get all rows."""
        return [list(row) for row in self.grid]
    
    def _cols(self) -> List[List[Cell]]:
        """Get all columns."""
        return [[self.grid[r][c] for r in range(ROWS)] for c in range(COLS)]
    
    def _diagonals(self) -> List[List[Cell]]:
        """Get all diagonals that could contain 4 pieces."""
        diagonals = []
        
        # Positive slope diagonals (/)
        for start_row in range(ROWS - FOUR + 1):
            for start_col in range(COLS - FOUR + 1):
                diag = []
                for i in range(ROWS):
                    r, c = start_row + i, start_col + i
                    if r < ROWS and c < COLS:
                        diag.append(self.grid[r][c])
                if len(diag) >= FOUR:
                    diagonals.append(diag)
        
        # Negative slope diagonals (\)
        for start_row in range(ROWS - FOUR + 1):
            for start_col in range(FOUR - 1, COLS):
                diag = []
                for i in range(ROWS):
                    r, c = start_row + i, start_col - i
                    if r < ROWS and c >= 0:
                        diag.append(self.grid[r][c])
                if len(diag) >= FOUR:
                    diagonals.append(diag)
        
        return diagonals
    
    def _check_line(self, line: List[Cell]) -> Optional[Cell]:
        """
        Check if a line contains 4 consecutive pieces of the same player.
        
        Args:
            line: A list of cells to check
            
        Returns:
            The winning player or None
        """
        for i in range(len(line) - FOUR + 1):
            window = line[i:i + FOUR]
            if all(cell == Cell.P1 for cell in window):
                return Cell.P1
            if all(cell == Cell.P2 for cell in window):
                return Cell.P2
        return None
