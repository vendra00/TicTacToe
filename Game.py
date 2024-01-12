import os
import random

from model.AI import AI
from model.Board import Board
from model.Player import Player
from model.enums.DifficultyLevel import DifficultyLevel
from model.enums.GameMode import GameMode
from model.enums.I18N import I18N
from model.enums.PiecePosition import PiecePosition
from model.enums.Symbol import Symbol
from utils.SoundController import play_sound, play_midi_file
from utils.Validators import validate_game_mode_input, validate_player_move_input, validate_difficulty_level_input, \
    validate_replay_input


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def simple_ai_move(board):
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board.board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else (None, None)


def game_setup(game_mode):
    player1_name = input(I18N.P1_NAME_REGISTER.value)
    player1 = Player(player1_name, Symbol.CROSS.value)
    play_sound('select')
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
        difficulty_input = input(I18N.CHOSE_AI_DIFFICULTY.value)

        # Check if the input is a valid difficulty level
        if validate_difficulty_level_input(difficulty_input):
            # Convert the valid input to the DifficultyLevel enum
            difficulty_level = DifficultyLevel(int(difficulty_input))
            play_sound('select')
            break
        else:
            print(I18N.INVALID_DIFFICULTY_LEVEL.value)
    player2 = AI(difficulty_level, Symbol.CIRCLE.value)
    return player2


def player_two_setup():
    player2_name = input(I18N.P2_NAME_REGISTER.value)
    player2 = Player(player2_name, Symbol.CIRCLE.value)
    play_sound('select')
    return player2


def game_start(board, current_player, player1, player2):
    while True:
        board.print_board()
        if isinstance(current_player, AI):
            row, col = current_player.make_move(board)
        else:
            move_position = get_player_move(current_player, board)
            row, col = position_to_coordinates(move_position)

        if not board.make_move(row, col, current_player.symbol):
            print(I18N.INVALID_MOVE.value)
            continue

        if board.check_tie():
            board.print_board()
            print(I18N.GAME_TIE.value)
            play_sound('draw')
            break

        if board.is_winner(current_player.symbol):
            board.print_board()
            winner_name = current_player.name if isinstance(current_player, Player) else I18N.AI.value
            print(f"{winner_name} {I18N.WIN.value}")
            play_sound('victory')
            break

        current_player = player2 if current_player == player1 else player1


def play_tic_tac_toe():
    play_midi_file('files/midi/Crystal_Doom.mid')
    while True:
        while True:
            game_mode_input = input(I18N.GAME_MODE.value)
            if validate_game_mode_input(game_mode_input):
                game_mode = int(game_mode_input)
                play_sound('select')
                break
            else:
                print(I18N.INVALID_GAME_MODE.value)

        player1, player2 = game_setup(game_mode)
        board = Board()
        current_player = player1

        game_start(board, current_player, player1, player2)

        while True:
            play_again = input(I18N.REPLAY.value)
            if validate_replay_input(play_again):
                if play_again.lower() in ['yes', 'y']:
                    play_sound('select')
                    break

                else:
                    print(I18N.THANKS.value)
                    play_sound('select')
                    return
            else:
                print(I18N.INVALID_REPLAY_INPUT.value)


def get_player_move(current_player, board):
    while True:
        try:
            move_input = input(f"{current_player.name} ({current_player.symbol}), {I18N.CHOSE_POSITION.value}")
            # Check if the input is valid
            if validate_player_move_input(move_input, board):
                # Convert the input to the PiecePosition enum
                move_position = PiecePosition(int(move_input))
                play_sound('valid_move')
                return move_position
            else:
                print(I18N.INVALID_POSITION.value)
                play_sound('invalid_move')

        except ValueError:
            print(I18N.INVALID_POSITION.value)


def position_to_coordinates(position):
    row = (position.value - 1) // 3
    col = (position.value - 1) % 3
    return row, col
