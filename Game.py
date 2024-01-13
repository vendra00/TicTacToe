import random
import time

from model.AI import AI
from model.Board import Board
from model.Player import Player
from model.enums.DifficultRatioAI import DifficultRatioAI
from model.enums.DifficultyLevel import DifficultyLevel
from model.enums.GameMode import GameMode
from model.enums.I18N import I18N
from model.enums.PiecePosition import PiecePosition
from model.enums.Symbol import Symbol
from utils.SoundController import play_sound, play_midi_file
from utils.Validators import validate_game_mode_input, validate_player_move_input, validate_difficulty_level_input, \
    validate_replay_input


def simple_ai_move(board):
    """
    Selects a move randomly from the available empty cells for the AI.

    Args:
        board (Board): The current state of the game board.

    Returns:
        tuple: The row and column of the chosen empty cell or (None, None) if no empty cells.
    """
    empty_cells = [(i, j) for i in range(3) for j in range(3) if board.board[i][j] == ' ']
    return random.choice(empty_cells) if empty_cells else (None, None)


def game_setup(game_mode):
    """
    Sets up the game based on the selected game mode, creating players or AI as needed.

    Args:
        game_mode (int): The selected game mode.

    Returns:
        tuple: Two Player objects representing player1 and player2.
    """
    player1_name = input(I18N.P1_NAME_REGISTER.value)
    player1 = Player(player1_name, Symbol.CROSS.value)
    play_sound('select')
    player2 = game_mode_setup(game_mode)
    return player1, player2


def game_mode_setup(game_mode):
    """
    Configures the second player based on the game mode.

    Args:
        game_mode (int): The game mode (multiplayer or single player or exit game).

    Returns:
        Player or None: The second player, either a human or an AI, or None if exiting the game.
    """
    if game_mode == GameMode.Multiplayer.value:
        return player_two_setup()
    elif game_mode == GameMode.SinglePlayer.value:
        return ai_difficult_setup()
    elif game_mode == GameMode.EXIT.value:
        print(I18N.THANKS.value)
        return None


def ai_difficult_setup():
    """
    Sets up the AI player with a chosen difficulty level.

    Returns:
        AI: The AI player with the selected difficulty level.
    """
    while True:
        difficulty_input = input(I18N.CHOSE_AI_DIFFICULTY.value)

        # Check if the input is a valid difficulty level
        if validate_difficulty_level_input(difficulty_input):
            # Convert the valid input to the DifficultyLevel enum
            difficulty_level = DifficultyLevel(int(difficulty_input))
            play_sound('select')
            if difficulty_level == DifficultyLevel.HARD:
                play_sound('hard')
            break
        else:
            print(I18N.INVALID_DIFFICULTY_LEVEL.value)
    player2 = AI(difficulty_level, Symbol.CIRCLE.value)
    return player2


def player_two_setup():
    """
    Sets up a human player as player two.

    Returns:
        Player: The second player.
    """
    player2_name = input(I18N.P2_NAME_REGISTER.value)
    player2 = Player(player2_name, Symbol.CIRCLE.value)
    play_sound('select')
    return player2


def game_start(board, current_player, player1, player2):
    """
    Starts and runs the game loop.

    Args:
        board (Board): The game board.
        current_player (Player or AI): The current player.
        player1 (Player): The first player.
        player2 (Player or AI): The second player.
    """
    while True:
        board.print_board()
        col, row = get_move(board, current_player)

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


def get_move(board, current_player):
    """
    Retrieves the next move from the current player. If the current player is AI,
    it adds a delay to simulate the AI "thinking" before making a move. If the
    current player is a human, it prompts the player for their move.

    Args:
        board (Board): The current state of the game board.
        current_player (Player or AI): The player (human or AI) who is currently making a move.
    Returns:
        tuple: A tuple (col, row) representing the column and row indices on the board where the move is made.
    """
    if isinstance(current_player, AI):
        print(I18N.AI_TURN.value)
        time.sleep(DifficultRatioAI.THINKING.value)
        row, col = current_player.make_move(board)
    else:
        move_position = get_player_move(current_player, board)
        row, col = position_to_coordinates(move_position)
    return col, row


def play_tic_tac_toe():
    """
    Initiates and controls the flow of the Tic Tac Toe game.
    """
    print(I18N.TITLE.value)
    play_midi_file('files/midi/Crystal_Doom.mid')
    while True:
        while True:
            game_mode_input = input(I18N.GAME_MODE.value)
            if validate_game_mode_input(game_mode_input):
                game_mode = int(game_mode_input)
                play_sound('select')
                if game_mode == GameMode.EXIT.value:
                    print(I18N.THANKS.value)
                    return
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
                    print(I18N.TITLE.value)
                    break

                else:
                    print(I18N.THANKS.value)
                    play_sound('select')
                    return
            else:
                print(I18N.INVALID_REPLAY_INPUT.value)


def get_player_move(current_player, board):
    """
    Obtains and validates the move from the current player.

    Args:
        current_player (Player): The player making the move.
        board (Board): The current state of the game board.

    Returns:
        PiecePosition: The position on the board where the player wants to make a move.
    """
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
    """
    Converts a PiecePosition enum value to board coordinates (row, col).

    Args:
        position (PiecePosition): The position on the board.

    Returns:
        tuple: Row and column indices corresponding to the position.
    """
    row = (position.value - 1) // 3
    col = (position.value - 1) % 3
    return row, col
