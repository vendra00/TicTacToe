from Game import game_setup, game_start
from model.Board import Board


def tic_tac_toe():
    while True:
        game_mode = input("Choose game mode: 1 for Player vs Player, 2 for Player vs AI: ")
        player1, player2 = game_setup(game_mode)
        board = Board()
        current_player = player1
        game_start(board, current_player, game_mode, player1, player2)

        play_again = input("Play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break


tic_tac_toe()
