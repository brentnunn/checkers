
import logging
import random
import checkerboard as cb
import checker as ch
from computerplayer import ComputerPlayer
from copy import deepcopy


logger = logging.getLogger(__name__)

class RandomPlayer(ComputerPlayer):
    """ This player makes random moves in the game of Checkers """

    def __init__(self):
        ComputerPlayer.__init__(self)
        random.seed()


    def evaluate_board(self):
        """ Evaluate the checkerboard, to determine next move """

        jumps_list = self.list_jumps()
        if jumps_list:
            return ('jump', random.choice(jumps_list))

        moves_list = self.list_moves()
        if moves_list:
            return ('move', random.choice(moves_list))

        return ('surrender',)


    def play(self):
        """ Determine action in game of checkers """

        evaluation = self.evaluate_board()
        if evaluation[0] == 'jump':
            self.jump_checkers(evaluation[1])
            print("Jump move completed")
            return "jump"

        elif evaluation[0] == 'move':
            self.move_checker(evaluation[1])
            print("Move completed")
            return "move"

        else:
            print("I surrender")
            return "surrender"

        


