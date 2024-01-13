from enum import Enum


class BoardStructure(Enum):
    """
    BoardStructure is an enumeration of the different string constants that represent
    the various parts of the board's structure in a Tic Tac Toe game when displayed in the console.
    """

    VERTICAL_LINE = '│'
    """A vertical line used to separate cells horizontally on the board."""

    TOP_BORDER = '┌───┬───┬───┐'
    """The top border of the board with intersections to create a T-shape for joining with the middle border."""

    MIDDLE_BORDER = '├───┼───┼───┤'
    """The middle border of the board that separates rows of cells and intersects to provide a continuous line 
    across."""

    BOTTOM_BORDER = '└───┴───┴───┘'
    """The bottom border of the board with intersections to cap the vertical lines."""
