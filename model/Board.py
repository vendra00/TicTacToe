# model/Board.py

from model.enums.BoardStructure import BoardStructure
from utils.BoardUtils import colorize


class Board:
    """
    Represents the Tic Tac Toe game board.

    Attributes:
        board (list of str): A 3x3 grid initialized with empty spaces.
    """
    def __init__(self):
        """
            Initializes a new empty Tic Tac Toe board.
        """
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        """
        Attempts to make a move on the board for a given player.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.
            player (str): The player symbol ('X' or 'O').

        Returns:
            bool: True if the move was made successfully, False otherwise.
        """
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False

    def is_valid_move(self, row, col):
        """
        Checks if a move is valid, i.e., if the cell is empty and within the board's bounds.

        Args:
            row (int): The row index of the move.
            col (int): The column index of the move.

        Returns:
            bool: True if the move is valid, False otherwise.
        """
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def check_tie(self):
        """
        Checks if the board is in a tie state.

        Returns:
            bool: True if the board has no empty spaces and there's no winner, False otherwise.
        """
        if all(all(cell != ' ' for cell in row) for row in self.board):
            return not (self.is_winner('X') or self.is_winner('O'))
        return False

    def print_board(self):
        """
        Prints the current state of the board to the console.
        """

        print("                    ")
        print(BoardStructure.TOP_BORDER.value)

        for i, row in enumerate(self.board):
            # Print the row with colorized cells
            row_str = ' ' + ' │ '.join(colorize(cell) for cell in row) + ' '
            print(f"{BoardStructure.VERTICAL_LINE.value}{row_str}{BoardStructure.VERTICAL_LINE.value}")

            # Print the middle border or bottom border
            if i < 2:  # Only print middle borders after the first and second row
                print(BoardStructure.MIDDLE_BORDER.value)
            else:
                print(BoardStructure.BOTTOM_BORDER.value)

    def is_winner(self, symbol):
        """
        Checks if a given player symbol has won the game.

        Args:
            symbol (str): The player symbol ('X' or 'O').

        Returns:
            bool: True if the player has won, False otherwise.
        """
        # Check rows for a win
        for i in range(3):
            if all(cell == symbol for cell in self.board[i]):
                return True
        # Check columns for a win
        for i in range(3):
            if all(cell == symbol for cell in self.board[i]) or \
                    all(self.board[j][i] == symbol for j in range(3)):  # Check columns
                return True
        # Check diagonals for a win
        if ((self.board[0][0] != self.board[1][1] or self.board[1][1] != self.board[2][2]
             or self.board[2][2] != symbol)  # Check diagonals
                and (self.board[0][2] != self.board[1][1] or self.board[1][1] != self.board[2][0]
                     or self.board[2][0] != symbol)):  # Check diagonals
            return False
        return True
