from model.enums.DifficultyLevel import DifficultyLevel
from model.enums.GameMode import GameMode


def validate_game_mode_input(input_str):
    return input_str.isdigit() and int(input_str) in [mode.value for mode in GameMode]


def validate_difficulty_level_input(input_str):
    return input_str.isdigit() and int(input_str) in [mode.value for mode in DifficultyLevel]


def validate_replay_input(input_str):
    return input_str.strip().lower() in ['yes', 'no'] and not any(char.isdigit() for char in input_str)


def validate_player_move_input(input_str, board):
    if not input_str.isdigit():
        return False
    position = int(input_str) - 1  # Subtract 1 to convert to 0-indexed position
    if not 0 <= position <= 8:  # Ensure the position is within the 0-8 range
        return False
    # Convert position to row and column, then check if the cell is empty
    row, col = position // 3, position % 3
    return board.board[row][col] == ' '

