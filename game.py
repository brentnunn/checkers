
import collections
import logging
from time import sleep
from checkerboard import Checkerboard
from checker import Checker
from player import Player
from computerplayer import ComputerPlayer
from simpleplayer import SimplePlayer


logger = logging.getLogger(__name__)

class Game:
    """ Controlling class for a game of checkers """

    def __init__(self, black_player, white_player):
        """ Initialize a new game """
        self.black_player = black_player
        self.white_player = white_player

        self.chb = Checkerboard()
        self.chb.setup_new_board()

        self.black_player.color = 'black'
        self.black_player.checkerboard = self.chb
        self.black_player.checkers = self.chb.black_checkers

        self.white_player.color = 'white'
        self.white_player.checkerboard = self.chb
        self.white_player.checkers = self.chb.white_checkers

        self.pos_counter = collections.Counter()

        
    def start_game():
        """ Begin play """
        pass


if __name__ == '__main__':
    #black_player = ComputerPlayer()
    logger.setLevel(logging.INFO)
    black_player = SimplePlayer()
    white_player = SimplePlayer()

    game = Game(black_player, white_player)

    game.chb.print_board()
    print('Starting game\n')
    
    turn = 'black'

    game_on = True
    while game_on:
        # Get hash value of all checkers' positions
        ch_black_pos = [ch.position for ch in black_player.checkers]
        ch_white_pos = [ch.position for ch in white_player.checkers]
        checkers_hash = hash(tuple(ch_black_pos + ch_white_pos))
        # Game ends in draw if all checkers' positions repeat 3 times
        #print('type(game.pos_counter) = {}'.format(type(game.pos_counter)))
        print('len(game.pos_counter) = {}'.format(len(game.pos_counter)))
        print('checkers_hash = {}'.format(checkers_hash))
        game.pos_counter.update([checkers_hash])
        print('game.pos_counter[checkers_hash] = {}'.format(game.pos_counter[checkers_hash]))
        if game.pos_counter[checkers_hash] >= 4:
            print('The game is a draw due to repeating positions')
            game_on = False
            break

        sleep(1)
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
        #print(msg)
        #print()

    print("Game over")
