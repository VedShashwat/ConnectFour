#!/usr/bin/env python3
"""Simple test runner for Connect Four project."""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from tests.test_board import (
    test_board_creation,
    test_drop_piece,
    test_legal_moves,
    test_winner_detection
)
from tests.test_ai import (
    test_ai_creation,
    test_ai_makes_move,
    test_ai_blocks_win
)


def run_tests():
    """Run all tests and report results."""
    tests = [
        ("Board Creation", test_board_creation),
        ("Drop Piece", test_drop_piece),
        ("Legal Moves", test_legal_moves),
        ("Winner Detection", test_winner_detection),
        ("AI Creation", test_ai_creation),
        ("AI Makes Move", test_ai_makes_move),
        ("AI Blocks Win", test_ai_blocks_win),
    ]
    
    passed = 0
    failed = 0
    
    print("Running tests\n")
    
    for name, test_func in tests:
        try:
            test_func()
            print(f"{name}")
            passed += 1
        except AssertionError as e:
            print(f" {name}: {e}")
            failed += 1
        except Exception as e:
            print(f" {name}: Unexpected error - {e}")
            failed += 1
    

    print(f"Results: {passed} passed, {failed} failed")
  
    
    return failed == 0


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
