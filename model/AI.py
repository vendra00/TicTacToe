import random

from model.DifficultyLevel import DifficultyLevel


class AI:
    def __init__(self, difficulty, symbol, name="AI"):
        self.difficulty = difficulty
        self.symbol = symbol
        self.name = name

    def make_move(self, board):
        if self.difficulty == DifficultyLevel.EASY:
            return self.easy_move(board)
        elif self.difficulty == DifficultyLevel.NORMAL:
            return self.normal_move(board)
        elif self.difficulty == DifficultyLevel.HARD:
            return self.hard_move(board)

    @staticmethod
    def easy_move(board):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board.board[i][j] == ' ']
        return random.choice(empty_cells) if empty_cells else (None, None)

    def normal_move(self, board):
        if random.random() < 0.55:
            best_move = self.best_move(board)
            if best_move:
                return best_move
        return AI.easy_move(board)  # Fallback to a random move

    def hard_move(self, board):
        if random.random() < 0.70:
            best_move = self.best_move(board)
            if best_move:
                return best_move
        return AI.easy_move(board)

    def best_move(self, board):
        # Check for a winning move first
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    board.board[i][j] = self.symbol
                    if self.is_winning_move(board, self.symbol):
                        board.board[i][j] = ' '  # Reset to empty
                        return i, j
                    board.board[i][j] = ' '  # Reset to empty

        # Check for a blocking move
        opponent_symbol = 'O' if self.symbol == 'X' else 'X'
        for i in range(3):
            for j in range(3):
                if board.board[i][j] == ' ':
                    board.board[i][j] = opponent_symbol
                    if self.is_winning_move(board, opponent_symbol):
                        board.board[i][j] = ' '  # Reset to empty
                        return i, j
                    board.board[i][j] = ' '  # Reset to empty

        return None

    @staticmethod
    def is_winning_move(board, symbol):
        # Check rows and columns
        for i in range(3):
            if all([cell == symbol for cell in board.board[i]]) or \
                    all([board.board[j][i] == symbol for j in range(3)]):
                return True
        # Check diagonals
        if board.board[0][0] == board.board[1][1] == board.board[2][2] == symbol or \
                board.board[0][2] == board.board[1][1] == board.board[2][0] == symbol:
            return True
        return False
