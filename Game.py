import os
import random

from model.AI import AI
from model.Board import Board
from model.Player import Player
from model.enums.DifficultyLevel import DifficultyLevel
from model.enums.GameMode import GameMode
from model.enums.PiecePosition import PiecePosition
from model.enums.Symbol import Symbol
from utils.Validators import validate_game_mode_input, validate_player_move_input, validate_difficulty_level_input, \
    validate_replay_input


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


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
    while True:
        difficulty_input = input("Choose AI difficulty: 1 for EASY, 2 for NORMAL, 3 for HARD: ")

        # Check if the input is a valid difficulty level
        if validate_difficulty_level_input(difficulty_input):
            # Convert the valid input to the DifficultyLevel enum
            difficulty_level = DifficultyLevel(int(difficulty_input))
            break
        else:
            print("Invalid input. Please enter a valid difficulty level: 1 for EASY, 2 for NORMAL, 3 for HARD.")
    player2 = AI(difficulty_level, Symbol.CIRCLE.value)
    return player2


def player_two_setup():
    player2_name = input("Enter name for Player 2: ")
    player2 = Player(player2_name, Symbol.CIRCLE.value)
    return player2


def game_start(board, current_player, game_mode, player1, player2):
    while True:
        board.print_board()
        if isinstance(current_player, AI):
            row, col = current_player.make_move(board)
        else:
            move_position = get_player_move(current_player, board)
            row, col = position_to_coordinates(move_position)

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

        while True:
            play_again = input("Play again? (yes/no): ")
            if validate_replay_input(play_again):
                if play_again.lower() in ['yes', 'y']:
                    break

                else:
                    print("Thanks for playing!")
                    return
            else:
                print("Invalid input. Please answer 'yes' or 'no'.")


def get_player_move(current_player, board):
    while True:
        try:
            move_input = input(f"{current_player.name} ({current_player.symbol}), choose a position (1-9): ")
            # Check if the input is valid
            if validate_player_move_input(move_input, board):
                # Convert the input to the PiecePosition enum
                move_position = PiecePosition(int(move_input))
                return move_position
            else:
                print(
                    "Invalid input or position already taken. Please enter a number between 1 and 9 for an empty spot.")

        except ValueError:
            print("Invalid input. Please enter a number between 1 and 9 for an empty spot.")


def position_to_coordinates(position):
    row = (position.value - 1) // 3
    col = (position.value - 1) % 3
    return row, col
