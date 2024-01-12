from enum import Enum


class I18N(Enum):
    P1_NAME_REGISTER = "Enter name for Player 1: "
    P2_NAME_REGISTER = "Enter name for Player 2: "
    CHOSE_AI_DIFFICULTY = "Choose AI difficulty: 1 for EASY, 2 for NORMAL, 3 for HARD: "
    INVALID_DIFFICULTY_LEVEL = ("Invalid input. Please enter a valid difficulty level: 1 for EASY, 2 for NORMAL, "
                                "3 for HARD.")
    INVALID_MOVE = "Invalid move, try again."
    GAME_TIE = "It's a tie!"
    WIN = "wins!"
    AI = "AI"
    GAME_MODE = "Choose game mode: 1 - for Player vs Player, 2 - for Player vs AI: "
    INVALID_GAME_MODE = "Invalid input. Please enter 1 for Player vs Player or 2 for Player vs AI."
    REPLAY = "Do you want to play again? (yes/no): "
    THANKS = "Thanks for playing!"
    INVALID_REPLAY_INPUT = "Invalid input. Please answer 'yes' or 'no'."
    CHOSE_POSITION = "choose a position (1-9): "
    INVALID_POSITION = ("Invalid input or position already taken. Please enter a number between 1 and 9 for an empty "
                        "spot.")
