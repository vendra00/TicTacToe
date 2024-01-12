def colorize(cell):
    if cell == 'X':
        return f'\033[91m{cell}\033[0m'  # Red for 'X'
    elif cell == 'O':
        return f'\033[94m{cell}\033[0m'  # Blue for 'O'
    return cell
