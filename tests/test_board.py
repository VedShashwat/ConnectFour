import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from board import Board, Cell

def test_board_creation():
    """Test that a new board is created correctly."""
    board = Board()
    assert len(board.grid) == 6
    assert len(board.grid[0]) == 7
    assert board.grid[0][0] == Cell.EMPTY

def test_drop_piece():
    """Test dropping a piece into the board."""
    board = Board()
    success = board.drop(0, Cell.P1)
    assert success == True
    assert board.grid[5][0] == Cell.P1  # Bottom row

def test_legal_moves():
    """Test getting legal moves from the board."""
    board = Board()
    moves = board.legal_moves()
    assert len(moves) == 7
    assert moves == [0, 1, 2, 3, 4, 5, 6]

def test_winner_detection():
    """Test basic winner detection."""
    board = Board()
    # Fill first row with P1 pieces
    for col in range(4):
        board.grid[5][col] = Cell.P1
    
    winner = board.winner()
    assert winner == Cell.P1
