# utils/Validators.py

from model.enums.DifficultyLevel import DifficultyLevel
from model.enums.GameMode import GameMode


def validate_game_mode_input(input_str):
    """
    Validate the game mode input.

    Args:
        input_str (str): The input string to validate.

    Returns:
        bool: True if input_str is a digit and corresponds to a valid game mode, False otherwise.
    """
    # Check if the input is a digit and convert to int, then verify it's a valid game mode
    return input_str.isdigit() and int(input_str) in [mode.value for mode in GameMode]


def validate_difficulty_level_input(input_str):
    """
    Validate the difficulty level input.

    Args:
        input_str (str): The input string to validate.

    Returns:
        bool: True if input_str is a digit and corresponds to a valid difficulty level, False otherwise.
    """
    # Check if the input is a digit and convert to int, then verify it's a valid difficulty level
    return input_str.isdigit() and int(input_str) in [mode.value for mode in DifficultyLevel]


def validate_replay_input(input_str):
    """
    Validate the replay input.

    Args:
        input_str (str): The input string to validate.

    Returns:
        bool: True if input_str is 'yes' or 'no', False otherwise.
    """
    # Strip leading/trailing whitespace, convert to lowercase, and check for 'yes' or 'no'
    # Also check that there are no digits in the input
    return input_str.strip().lower() in ['yes', 'no', 'y', 'n'] and not any(char.isdigit() for char in input_str)


def validate_player_move_input(input_str, board):
    """
    Validate the player move input.

    Args:
        input_str (str): The input string to validate.
        board (Board): The current state of the board.

    Returns:
        bool: True if input_str is a valid move (i.e., a digit representing an empty cell on the board),
        False otherwise.
    """
    # Check if the input is a digit
    if not input_str.isdigit():
        return False

    # Convert to a 0-indexed board position
    position = int(input_str) - 1

    # Ensure the position is within the 0-8 range for a 3x3 board
    if not 0 <= position <= 8:
        return False

    # Convert the position to row and column indices
    row, col = position // 3, position % 3

    # Return True if the selected cell is empty, False otherwise
    return board.board[row][col] == ' '
