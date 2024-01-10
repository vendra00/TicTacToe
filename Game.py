import random

from model.AI import AI
from model.Board import Board
from model.DifficultyLevel import DifficultyLevel
from model.GameMode import GameMode
from model.Player import Player
from model.Symbol import Symbol
from utils.Validators import validate_game_mode_input


def simple_ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board.board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else (None, None)


def game_setup(game_mode):
    player1_name = input("Enter name for Player 1: ")
    player1 = Player(player1_name, Symbol.CROSS.value)
    player2 = game_mode_setup(game_mode)
    return player1, player2


def game_mode_setup(game_mode):
    if game_mode == GameMode.Multiplayer.value:
        player2 = player_two_setup()
        return player2
    if game_mode == GameMode.SinglePlayer.value:
        player2 = ai_difficult_setup()
        return player2


def ai_difficult_setup():
    difficulty = input("Choose AI difficulty: 1 for EASY, 2 for NORMAL, 3 for HARD: ")
    difficulty_level = DifficultyLevel([DifficultyLevel.EASY, DifficultyLevel.NORMAL, DifficultyLevel.HARD]
                                       [int(difficulty) - 1])
    player2 = AI(difficulty_level, Symbol.CIRCLE.value)
    return player2


def player_two_setup():
    player2_name = input("Enter name for Player 2: ")
    player2 = Player(player2_name, Symbol.CIRCLE.value)
    return player2


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
        while True:
            game_mode_input = input("Choose game mode: 1 for Player vs Player, 2 for Player vs AI: ")
            if validate_game_mode_input(game_mode_input):
                game_mode = int(game_mode_input)
                break
            else:
                print("Invalid input. Please enter 1 for Player vs Player or 2 for Player vs AI.")

        player1, player2 = game_setup(game_mode)
        board = Board()
        current_player = player1

        game_start(board, current_player, game_mode, player1, player2)

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break
