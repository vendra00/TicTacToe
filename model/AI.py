# model/AI.py

import random

from model.enums.DifficultRatioAI import DifficultRatioAI
from model.enums.DifficultyLevel import DifficultyLevel
from model.enums.I18N import I18N


class AI:
    """
    Represents an AI player in the Tic Tac Toe game with varying difficulty levels.

    Attributes:
        difficulty (DifficultyLevel): The difficulty level of the AI.
        symbol (str): The symbol used by the AI on the board ('X' or 'O').
        name (str): The name of the AI player.
    """

    def __init__(self, difficulty, symbol, name=I18N.AI.value):
        """
        Initialize the AI with a set difficulty level, symbol, and name.

        Args:
            difficulty (DifficultyLevel): The difficulty level of the AI.
            symbol (str): The symbol used by the AI on the board.
            name (str, optional): The name of the AI player. Defaults to "AI".
        """
        self.difficulty = difficulty
        self.symbol = symbol
        self.name = name

    def make_move(self, board):
        """
        Make a move on the board based on the AI's difficulty level.

        Args:
            board (Board): The current state of the board.

        Returns:
            tuple: The row and column where the AI has decided to make a move.
        """
        if self.difficulty == DifficultyLevel.EASY:
            return self.easy_move(board)
        elif self.difficulty == DifficultyLevel.NORMAL:
            return self.normal_move(board)
        elif self.difficulty == DifficultyLevel.HARD:
            return self.hard_move(board)

    @staticmethod
    def easy_move(board):
        """
        Choose a move randomly from the available empty cells for the EASY difficulty level.

        Args:
            board (Board): The current state of the board.

        Returns:
            tuple: The row and column of the chosen empty cell or (None, None) if no empty cells.
        """
        empty_cells = [(i, j) for i in range(3) for j in range(3) if board.board[i][j] == ' ']
        return random.choice(empty_cells) if empty_cells else (None, None)

    def normal_move(self, board):
        """
        For the NORMAL difficulty level, make a best move with a certain probability or fall back to a random move.

        Args:
            board (Board): The current state of the board.

        Returns:
            tuple: The row and column of the chosen move.
        """
        if random.random() < DifficultRatioAI.NORMAL.value:
            best_move = self.best_move(board)
            if best_move:
                return best_move
        return AI.easy_move(board)  # Fallback to a random move

    def hard_move(self, board):
        """
        For the HARD difficulty level, make a best move with a higher probability or fall back to a random move.

        Args:
            board (Board): The current state of the board.

        Returns:
            tuple: The row and column of the chosen move.
        """
        if random.random() < DifficultRatioAI.HARD.value:
            best_move = self.best_move(board)
            if best_move:
                return best_move
        return AI.easy_move(board)

    def best_move(self, board):
        """
        Determine the best move by checking for a winning move or blocking the opponent's winning move.

        Args:
            board (Board): The current state of the board.

        Returns:
            tuple: The row and column of the best move, or None if no best move is found.
        """
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
        """
        Check if a move is a winning move for a given symbol.

        Args:
            board (Board): The current state of the board.
            symbol (str): The symbol ('X' or 'O') to check for a winning move.

        Returns:
            bool: True if the move is a winning move, False otherwise.
        """
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
