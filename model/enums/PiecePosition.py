# model/enums/BoardStructure.py

from enum import Enum


class PiecePosition(Enum):
    """
    PiecePosition is an enumeration that represents the positions on a Tic Tac Toe board.
    Each position is associated with a unique integer that players can input to place their piece.
    """

    TOP_LEFT = 1
    """The top-left position on the Tic Tac Toe board."""

    TOP_CENTER = 2
    """The top-center position on the Tic Tac Toe board."""

    TOP_RIGHT = 3
    """The top-right position on the Tic Tac Toe board."""

    MIDDLE_LEFT = 4
    """The middle-left position on the Tic Tac Toe board."""

    MIDDLE_CENTER = 5
    """The center position on the Tic Tac Toe board, also known as the 'center square'."""

    MIDDLE_RIGHT = 6
    """The middle-right position on the Tic Tac Toe board."""

    BOTTOM_LEFT = 7
    """The bottom-left position on the Tic Tac Toe board."""

    BOTTOM_CENTER = 8
    """The bottom-center position on the Tic Tac Toe board."""

    BOTTOM_RIGHT = 9
    """The bottom-right position on the Tic Tac Toe board."""
