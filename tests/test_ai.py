import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from board import Board, Cell
from ai import MinimaxAI

def test_ai_creation():
    """Test that AI can be created."""
    ai = MinimaxAI(Cell.P2)
    assert ai.player == Cell.P2
    assert ai.depth == 4

def test_ai_makes_move():
    """Test that AI can make a move."""
    board = Board()
    ai = MinimaxAI(Cell.P2)
    move = ai.best_move(board)
    assert 0 <= move < 7
    assert move in board.legal_moves()

def test_ai_blocks_win():
    """Test that AI blocks opponent's winning move."""
    board = Board()
    # Set up a situation where P1 is about to win
    board.grid[5][0] = Cell.P1
    board.grid[5][1] = Cell.P1
    board.grid[5][2] = Cell.P1
    # P1 needs column 3 to win
    
    ai = MinimaxAI(Cell.P2)
    move = ai.best_move(board)
    # AI should block by playing in column 3
    assert move == 3
