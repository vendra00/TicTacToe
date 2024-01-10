import random

from model.AI import AI
from model.Board import Board
from model.DifficultyLevel import DifficultyLevel
from model.Player import Player


def simple_ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board.board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else (None, None)


def game_setup(game_mode):
    player1_name = input("Enter name for Player 1: ")
    player1 = Player(player1_name, 'X')
    if game_mode == '1':
        player2_name = input("Enter name for Player 2: ")
        player2 = Player(player2_name, 'O')
    else:
        difficulty = input("Choose AI difficulty: 1 for EASY, 2 for NORMAL, 3 for HARD: ")
        difficulty_level = DifficultyLevel([DifficultyLevel.EASY, DifficultyLevel.NORMAL, DifficultyLevel.HARD]
                                           [int(difficulty) - 1])
        player2 = AI(difficulty_level, 'O')  # Pass 'O' as the symbol for the AI
    return player1, player2


def game_start(board, current_player, game_mode, player1, player2):
    while True:
        board.print_board()
        if current_player == player2 and game_mode != '1':
            row, col = simple_ai_move(board)
            print(f"AI chose row {row}, column {col}")
        else:
            row, col = current_player.make_move(board)

        if not board.make_move(row, col, current_player.symbol):
            print("Invalid move, try again.")
            continue

        if board.check_tie():
            board.print_board()
            print("It's a tie!")
            break

        if board.is_winner(current_player.symbol):
            board.print_board()
            winner_name = current_player.name if isinstance(current_player, Player) else "AI"
            print(f"{winner_name} wins!")
            break

        current_player = player2 if current_player == player1 else player1


def play_tic_tac_toe():
    while True:
        game_mode = input("Choose game mode: 1 for Player vs Player, 2 for Player vs AI: ")
        player1, player2 = game_setup(game_mode)
        board = Board()
        current_player = player1
        game_start(board, current_player, game_mode, player1, player2)

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
