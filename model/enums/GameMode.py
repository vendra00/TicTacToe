# model/enums/GameMode.py

from enum import Enum


class GameMode(Enum):
    """
    GameMode is an enumeration of the different game modes available in the Tic Tac Toe game.
    """

    Multiplayer = 1
    """ The multiplayer game mode where two human players play against each other. """

    SinglePlayer = 2
    """ The single player game mode where a human player plays against an AI. """
