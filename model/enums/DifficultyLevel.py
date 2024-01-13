# model/enums/DifficultyLevel.py

from enum import Enum


class DifficultyLevel(Enum):
    """
    DifficultyLevel is an enumeration of the different difficulty levels for the AI player in a Tic Tac Toe game.
    """

    EASY = 1
    """ The EASY difficulty level """

    NORMAL = 2
    """ The NORMAL difficulty level """

    HARD = 3
    """ The HARD difficulty level """
