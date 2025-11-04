import logging
from board import Board, Cell
from ai import MinimaxAI

logging.basicConfig(level=logging.INFO, format="%(message)s")

ROWS, COLS = 6, 7

def play_game(vs_ai: bool = True) -> None:
    board = Board()
    ai = MinimaxAI(Cell.P2) if vs_ai else None
    current = Cell.P1

    logging.info("Welcome to Connect Four!\n")
    while True:
        logging.info("\n" + str(board))
        if current == Cell.P1 or not vs_ai:
            move = _human_move(board, current)
        else:
            move = ai.best_move(board)
            logging.info(f"AI selects column {move}")

        board.drop(move, current)

        if board.winner():
            logging.info("\n" + str(board))
            logging.info(f"\n🎉  Player {current.name} wins!")
            break
        if board.is_full():
            logging.info("\n" + str(board))
            logging.info("\n🤝  The game is a draw.")
            break

        current = Cell.P1 if current == Cell.P2 else Cell.P2

def _human_move(board: Board, player: Cell) -> int:
    while True:
        try:
            col = int(input(f"Player {player.name}, choose a column (0-{COLS-1}): "))
            if col in board.legal_moves():
                return col
        except ValueError:
            pass
        logging.info("Invalid move, try again.")

if __name__ == "__main__":
    play_game(vs_ai=True)  # set False for human vs human
