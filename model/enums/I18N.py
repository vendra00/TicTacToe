# model/enums/I18N.py

from enum import Enum


class I18N(Enum):
    """
    I18N (Internationalization) contains a set of messages and prompts used in the Tic Tac Toe game.
    These messages include prompts for player actions, game status updates, and ASCII art for the game title.
    ANSI escape codes are used to add formatting such as bold text and colored text for various prompts.
    """

    TITLE = """
    ████████╗██╗ ██████╗    ████████╗ █████╗  ██████╗    ████████╗ ██████╗ ███████╗    ██████╗  █████╗  ██████╗ ███████╗    
    ╚══██╔══╝██║██╔════╝    ╚══██╔══╝██╔══██╗██╔════╝    ╚══██╔══╝██╔═══██╗██╔════╝    ██╔══██╗██╔══██╗██╔════╝ ██╔════╝    
       ██║   ██║██║            ██║   ███████║██║            ██║   ██║   ██║█████╗      ██████╔╝███████║██║  ███╗█████╗      
       ██║   ██║██║            ██║   ██╔══██║██║            ██║   ██║   ██║██╔══╝      ██╔══██╗██╔══██║██║   ██║██╔══╝      
       ██║   ██║╚██████╗       ██║   ██║  ██║╚██████╗       ██║   ╚██████╔╝███████╗    ██║  ██║██║  ██║╚██████╔╝███████╗
    """
    """ ASCII art representing the game title "TIC TAC TOE RAGE". """

    P1_NAME_REGISTER = "\033[1m      Enter name for Player 1: \033[0m"
    """ Prompt for entering the name of Player 1 with bold formatting. """

    P2_NAME_REGISTER = "\033[1m      Enter name for Player 2: \033[0m"
    """ Prompt for entering the name of Player 2 with bold formatting. """

    CHOSE_AI_DIFFICULTY = ("\033[1m      Choose AI difficulty: \033[0m"
                           "\n        \033[92m1 - EASY\033[0m"  # Green for EASY
                           "\n        \033[93m2 - NORMAL\033[0m"  # Yellow for NORMAL
                           "\n        \033[91m3 - HARD\033[0m"  # Red for HARD
                           "\n        Your choice: ")
    """ Prompt for choosing the AI difficulty with color-coded options. """

    INVALID_DIFFICULTY_LEVEL = ("Invalid input. Please enter a valid difficulty level: 1 for EASY, 2 for NORMAL, "
                                "3 for HARD.")
    """ Error message for invalid difficulty level input. """

    INVALID_MOVE = "Invalid move, try again."
    """ Error message for invalid move input. """

    GAME_TIE = "It's a tie!"
    """ Message for a tie game. """

    WIN = "wins!"
    """ Message for a win. """

    AI = "AI"
    """ String constant for the AI player. """

    GAME_MODE = ("\033[1m      Choose Game Mode: \033[0m"
                 "\n        1 - for Player vs Player, "
                 "\n        2 - for Player vs AI "
                 "\n        Your choice: ")
    """ Prompt for choosing the game mode. """

    INVALID_GAME_MODE = "Invalid input. Please enter 1 for Player vs Player or 2 for Player vs AI."
    """ Error message for invalid game mode input. """

    REPLAY = "\033[1m       Do you want to play again? (yes/no): \033[0m"
    """ Prompt for replaying the game. """

    THANKS = "Thanks for playing!"
    """ Message for ending the game. """

    INVALID_REPLAY_INPUT = "Invalid input. Please answer 'yes' or 'no'."
    """ Error message for invalid replay input. """

    CHOSE_POSITION = "choose a position (1-9): "
    """ Prompt for choosing a position on the board. """

    INVALID_POSITION = ("Invalid input or position already taken. Please enter a number between 1 and 9 for an empty "
                        "spot.")
    """ Error message for invalid position input. """
