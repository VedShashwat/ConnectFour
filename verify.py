#!/usr/bin/env python3
"""Verify the Connect Four game works correctly."""

from board import Board, Cell
from ai import MinimaxAI


def test_complete_game():
    """Test a complete game scenario."""
    print("Testing Connect Four implementation.\n")
    
    # Test 1: Board creation
    print(" Test 1: Creating board...")
    board = Board()
    assert len(board.grid) == 6
    assert len(board.grid[0]) == 7
    print(board)
    
    # Test 2: Dropping pieces
    print("\n Test 2: Dropping pieces...")
    board.drop(0, Cell.P1)
    board.drop(1, Cell.P2)
    board.drop(0, Cell.P1)
    print(board)
    
    # Test 3: AI creation and move
    print("\n Test 3: AI makes a move...")
    ai = MinimaxAI(Cell.P2, depth=3)
    move = ai.best_move(board)
    print(f"AI chose column {move}")
    board.drop(move, Cell.P2)
    print(board)
    
    # Test 4: Winning scenario
    print("\n Test 4: Testing winner detection...")
    board2 = Board()
    for col in range(4):
        board2.grid[5][col] = Cell.P1
    winner = board2.winner()
    assert winner == Cell.P1
    print(f"Winner detected: {winner.name}")
    print(board2)
    
    # Test 5: AI blocks winning move
    print("\n Test 5: AI blocks opponent's win...")
    board3 = Board()
    board3.grid[5][0] = Cell.P1
    board3.grid[5][1] = Cell.P1
    board3.grid[5][2] = Cell.P1
    ai2 = MinimaxAI(Cell.P2, depth=4)
    blocking_move = ai2.best_move(board3)
    print(f"AI blocks at column {blocking_move}")
    assert blocking_move == 3
    print(board3)
    
    
    print("All tests passed! ")
    
    print("\nThe Connect Four game is fully functional!")
    print("Run 'python cli.py' to play the game.")


if __name__ == "__main__":
    test_complete_game()
