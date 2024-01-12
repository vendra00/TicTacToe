from model.enums.DifficultyLevel import DifficultyLevel
from model.enums.GameMode import GameMode


def validate_game_mode_input(input_str):
    return input_str.isdigit() and int(input_str) in [mode.value for mode in GameMode]


def validate_difficulty_level_input(input_str):
    return input_str.isdigit() and int(input_str) in [mode.value for mode in DifficultyLevel]


def validate_player_move_input(input_str, board):
    if not input_str.isdigit():
        return False
    position = int(input_str)
    return 0 <= position < len(board.board) * len(board.board[0]) and board.board[position // 3][position % 3] == ' '
