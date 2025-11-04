# Connect Four Game

A fully functional Connect Four game implementation in Python with AI opponent using Minimax algorithm with alpha-beta pruning.

## Features

- **Complete Connect Four gameplay** with standard 6x7 board
- **AI opponent** using Minimax algorithm with alpha-beta pruning
- **Heuristic evaluation** for intelligent AI moves
- **Human vs AI** or **Human vs Human** modes
- **Comprehensive test suite** for board logic and AI behavior
- **Command-line interface** for easy gameplay

## Project Structure

```
Connect_Four/
├── board.py          # Board class with game logic
├── ai.py             # MinimaxAI implementation
├── cli.py            # Command-line interface
├── verify.py         # Verification script
├── run_tests.py      # Test runner
├── tests/
│   ├── __init__.py
│   ├── test_board.py # Board tests
│   └── test_ai.py    # AI tests
└── README.md         # This file
```

## Components

### board.py
- `Cell` enum: Represents cell states (EMPTY, P1, P2)
- `Board` class: Game board with methods for:
  - Dropping pieces
  - Checking legal moves
  - Detecting winners (rows, columns, diagonals)
  - Board display and copying

### ai.py
- `MinimaxAI` class: AI player using:
  - Minimax algorithm with alpha-beta pruning
  - Configurable search depth (default: 4)
  - Heuristic evaluation function
  - Strategic position scoring

### cli.py
- Game loop for playing Connect Four
- Human input handling
- AI move execution
- Game state display

## How to Play

### Start the Game

```bash
python cli.py
```

### Game Modes

- **Human vs AI** (default): Set `vs_ai=True` in `cli.py`
- **Human vs Human**: Set `vs_ai=False` in `cli.py`

### Gameplay

1. The board displays with column numbers (0-6)
2. Player 1 (X) goes first
3. Enter column number to drop your piece
4. AI (O) responds automatically
5. First to connect 4 wins!

### Board Display

```
  0 1 2 3 4 5 6
  -------------
  . . . . . . .
  . . . . . . .
  . . . . . . .
  . . . . . . .
  X . . . . . .
  X O . O . . .
```

- `.` = Empty cell
- `X` = Player 1
- `O` = Player 2 (AI)

## Testing

### Run Verification Script

```bash
python verify.py
```

This runs automated tests covering:
- Board creation
- Piece dropping
- AI decision making
- Winner detection
- AI blocking strategy

### Run Test Suite

```bash
python run_tests.py
```

Or run individual test files:

```bash
python tests/test_board.py
python tests/test_ai.py
```

## Implementation Details

### AI Algorithm

The AI uses **Minimax with Alpha-Beta Pruning**:
- Searches game tree to configurable depth
- Evaluates positions using heuristics:
  - Center column preference (+3 points per piece)
  - Window evaluation (2, 3, 4 in a row)
  - Blocking opponent threats
  - Immediate win/loss detection

### Winning Conditions

The game checks for 4 consecutive pieces in:
- Horizontal rows
- Vertical columns
- Diagonal lines (both directions)

## Requirements

- Python 3.6+
- No external dependencies required




