from enum import Enum


class DifficultRatioAI(Enum):
    """
    DifficultRatioAI is an enumeration of the different difficulty levels for the AI player in a Tic Tac Toe game.
    Each difficulty level has a ratio value that determines the probability of the AI making the best move.
    """

    NORMAL = 0.55
    """ The NORMAL difficulty level has a ratio of 0.55, which means that the AI has a 55% chance of making the best """

    HARD = 0.70
    """The HARD difficulty level has a ratio of 0.70, which means that the AI has a 70% chance of making the best 
    move."""

    THINKING = 1.33
    """The THINKING  level has a ratio of 1.33, which means that the AI has a 1.33 second delay in the play move."""
