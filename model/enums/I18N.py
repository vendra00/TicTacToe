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
                 "\n        1 - Multiplayer (Local)"
                 "\n        2 - Single Player"
                 "\n        3 - Multiplayer (Remote)"
                 "\n        0 - Exit"
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

    AI_TURN = "AI is thinking..."
    """ Message for when the AI is thinking. """

    HOST_IP = "Enter the host's IP address: "
    """ Prompt for entering the host's IP address. """

    HOST_PORT = "Enter the host's port: "
    """ Prompt for entering the host's port. """

    JOIN_GAME = "Joining game..."
    """ Message for when the player is joining a game. """

    CREATE_GAME = "Creating game..."
    """ Message for when the player is creating a game. """

    CONNECTED = "Connected!"
    """ Message for when the player is connected to the remote player. """

    WAITING_PLAYER_CONNECT = "Waiting for other player to connect..."
    """ Message for when the player is waiting for the other player to connect. """

    REMOTE_PROMPT = "\033[1m      Do you want to (4) host or (5) join a game?  \033[0m"
    """ Prompt for choosing to host or join a game. """

    FAILED_TO_CONNECT = "Failed to connect. Please check the IP address and port and try again."
    """ Error message for failed connection. """

    INVALID_REMOTE_INPUT = "Invalid input. Please enter 4 to host a game or 5 to join a game."
    """ Error message for invalid remote input. """

    GAME_HOSTED = "Game hosted at {host_ip}:{host_port}"
    """ Message for when the game is hosted. """
