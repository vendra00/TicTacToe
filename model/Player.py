# model/Player.py

class Player:
    """
    Represents a player in the Tic Tac Toe game.

    Attributes:
        name (str): The name of the player.
        symbol (str): The symbol assigned to the player ('X' or 'O').
    """
    def __init__(self, name, symbol):
        """
        Initializes a new player with a given name and symbol.

        Args:
            name (str): The name of the player.
            symbol (str): The symbol assigned to the player ('X' or 'O').
        """
        self.name = name
        self.symbol = symbol

