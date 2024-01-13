# utils/BoardUtils.py

def colorize(cell):
    """
    Applies ANSI color codes to a given cell character for display in the console.

    This function is used to enhance the visual representation of the game board in the console
    by coloring the 'X' and 'O' symbols.

    Args:
        cell (str): The cell character to colorize ('X', 'O', or empty space).

    Returns:
        str: The colorized cell character. 'X' is colored red, 'O' is colored blue, and empty spaces are left uncolored.
    """
    if cell == 'X':
        return f'\033[91m{cell}\033[0m'  # Red for 'X'
    elif cell == 'O':
        return f'\033[94m{cell}\033[0m'  # Blue for 'O'
    return cell
