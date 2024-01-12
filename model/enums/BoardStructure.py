from enum import Enum


class BoardStructure(Enum):
    VERTICAL_LINE = '│'
    TOP_BORDER = '┌───┬───┬───┐'
    MIDDLE_BORDER = '├───┼───┼───┤'
    BOTTOM_BORDER = '└───┴───┴───┘'
