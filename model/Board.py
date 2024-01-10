# model/Board.py

class Board:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

    def make_move(self, row, col, player):
        if self.is_valid_move(row, col):
            self.board[row][col] = player
            return True
        return False

    def is_valid_move(self, row, col):
        return 0 <= row < 3 and 0 <= col < 3 and self.board[row][col] == ' '

    def check_tie(self):
        if all(all(cell != ' ' for cell in row) for row in self.board):
            return not (self.is_winner('X') or self.is_winner('O'))
        return False

    def print_board(self):
        for row in self.board:
            print(" | ".join(row))
            print("-" * 5)

    def is_winner(self, symbol):
        # Check rows and columns
        for i in range(3):
            if all(cell == symbol for cell in self.board[i]) or \
                    all(self.board[j][i] == symbol for j in range(3)):
                return True
        if (self.board[0][0] != self.board[1][1] or self.board[1][1] != self.board[2][2] or self.board[2][
            2] != symbol) and (
                self.board[0][2] != self.board[1][1] or self.board[1][1] != self.board[2][0] or self.board[2][
            0] != symbol):
            return False
        # Check diagonals
        return True
