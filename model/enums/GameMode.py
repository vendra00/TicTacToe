# model/enums/GameMode.py

from enum import Enum


class GameMode(Enum):
    """
    GameMode is an enumeration of the different game modes available in the Tic Tac Toe game.
    """

    EXIT = 0
    """ The exit game mode where the game is terminated. """

    MULTIPLAYER = 1
    """ The multiplayer game mode where two human players play against each other. """

    SINGLE_PLAYER = 2
    """ The single player game mode where a human player plays against an AI. """

    REMOTE_MULTIPLAYER = 3
    """ The remote multiplayer game mode where two human players play against each other. """

    CREATE_GAME = 4
    """ The create game mode where a human player creates a game. """

    JOIN_GAME = 5
    """ The join game mode where a human player joins a game. """
