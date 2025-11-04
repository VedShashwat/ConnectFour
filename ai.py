from typing import List, Optional, Tuple
import math
import random
from board import Board, Cell, ROWS, COLS, FOUR

EvalScore = int

class MinimaxAI:
    def __init__(self, player: Cell, depth: int = 4):
        self.player = player
        self.depth = depth

    def best_move(self, board: Board) -> int:
        _, move = self._minimax(board, self.depth, -math.inf, math.inf, True)
        return move if move is not None else random.choice(board.legal_moves())

    def _minimax(self, board: Board, depth: int, alpha: float, beta: float, maximizing: bool) -> Tuple[EvalScore, Optional[int]]:
        winner = board.winner()
        if winner == self.player:
            return 10_000 + depth, None
        if winner is not None:
            return -10_000 - depth, None
        if depth == 0 or board.is_full():
            return self._heuristic(board), None

        best_move: Optional[int] = None
        if maximizing:
            max_eval = -math.inf
            for move in board.legal_moves():
                child = board.copy()
                child.drop(move, self.player)
                eval_, _ = self._minimax(child, depth - 1, alpha, beta, False)
                if eval_ > max_eval:
                    max_eval, best_move = eval_, move
                alpha = max(alpha, eval_)
                if beta <= alpha:
                    break
            return max_eval, best_move
        else:
            min_eval = math.inf
            opp = Cell.P1 if self.player == Cell.P2 else Cell.P2
            for move in board.legal_moves():
                child = board.copy()
                child.drop(move, opp)
                eval_, _ = self._minimax(child, depth - 1, alpha, beta, True)
                if eval_ < min_eval:
                    min_eval, best_move = eval_, move
                beta = min(beta, eval_)
                if beta <= alpha:
                    break
            return min_eval, best_move

    def _heuristic(self, board: Board) -> EvalScore:
        score = 0
        center_array = [board.grid[r][COLS // 2] for r in range(ROWS)]
        score += center_array.count(self.player) * 3

        for line in board._rows() + board._cols() + board._diagonals():
            score += self._score_line(line)
        return score

    def _score_line(self, line: List[Cell]) -> EvalScore:
        score = 0
        opp = Cell.P1 if self.player == Cell.P2 else Cell.P2
        for i in range(len(line) - FOUR + 1):
            window = line[i : i + FOUR]
            score += self._evaluate_window(window, self.player, opp)
        return score

    @staticmethod
    def _evaluate_window(window: List[Cell], player: Cell, opp: Cell) -> EvalScore:
        count_p = window.count(player)
        count_o = window.count(opp)
        count_e = window.count(Cell.EMPTY)
        if count_p == 4:
            return 1_000
        if count_p == 3 and count_e == 1:
            return 5
        if count_p == 2 and count_e == 2:
            return 2
        if count_o == 3 and count_e == 1:
            return -4
        return 0
