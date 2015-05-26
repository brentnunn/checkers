
import logging
from time import sleep
from checkerboard import Checkerboard
from checker import Checker
from player import Player
from computerplayer import ComputerPlayer


logger = logging.getLogger(__name__)

class Game:
    """ Controlling class for a game of checkers """

    def __init__(self, black_player, white_player):
        """ Initialize a new game """
        self.black_player = black_player
        self.white_player = white_player

        self.chb = Checkerboard()
        self.chb.setup_new_board()

        self.black_player.checkerboard = self.chb
        self.black_player.checkers = self.chb.black_checkers

        self.white_player.checkerboard = self.chb
        self.white_player.checkers = self.chb.white_checkers

        
    def start_game():
        """ Begin play """
        pass


if __name__ == '__main__':
    black_player = ComputerPlayer()
    white_player = ComputerPlayer()

    game = Game(black_player, white_player)

    game.chb.print_board()
    print('Starting game\n')
    
    turn = 'black'

    game_on = True
    while game_on:
        sleep(4)
        if turn == 'black':
            if black_player.play() == 'surrender':
                msg = 'Black surrenders'
                game_on = False
            else:
                msg = 'Black move complete'
                turn = 'white'
        else:
            if white_player.play() == 'surrender':
                msg = 'White surrenders'
                game_on = False
            else:
                msg = 'White move complete'
                turn = 'black'

        game.chb.print_board()
        print(msg)
        print()

    print("Game over")
