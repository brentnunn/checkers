
from checkerboard import Checkerboard as cb
from checker import Checker as ch
from player import Player as pl

class Game:
    """ Controlling class for a game of checkers """

    def __init__(self, black_player, white_player):
        """ Initialize a new game """
        self.black_player = black_player
        self.white_player = white_player

        self.chb = Checkerboard()
        self.chb.setup_new_board()

        self.black_player.checkerboard = self.chb
        self.black_player.checkers = chb.black_checkers

        self.white_player.checkerboard = self.chb
        self.white_player.checkers = chb.white_checkers

        
    def start_game():
        """ Begin play """
        pass


