
import logging
import checkerboard as cb
import checker as ch
from player import Player
from copy import deepcopy

logger = logging.getLogger(__name__)

class ComputerPlayer(Player):
    """ Computer based Player for the game of Checkers """

    def __init__(self):
        Player.__init__(self)


    def list_jumps(self):
        """ Return list of all available jumps """

        jumps_list = []
        for ch in self.checkers:
            jumps = ch.list_jumps()
            if jumps:
                jumps_list.extend(deepcopy(jumps))

        return jumps_list


    def list_moves(self):
        """ Returns list of all available checker moves """

        moves_list = []
        for ch in self.checkers:
            moves = ch.list_moves()
            if moves:
                moves_list.extend(deepcopy(moves))

        return moves_list


    def move_checker(self, move_squares):
        """ Move checker at move_squares[0] to move_squares[1] """

        self.checkerboard.get_checker(move_squares[0]).move(move_squares[1])


    def jump_checkers(self, jump_squares):
        """ The checker at jump_squares[0] will jump to the other squares in the list.
            This will execute all jumps in the list. """

        self.checkerboard.get_checker(jump_squares[0]).jump_chain(jump_squares)


