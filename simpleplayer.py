
import logging
import random
import checkerboard as cb
import checker as ch
from computerplayer import ComputerPlayer
from copy import deepcopy


logger = logging.getLogger(__name__)

class SimplePlayer(ComputerPlayer):
    """ This player uses simple heuristics to make moves in the game of Checkers """

    def __init__(self):
        ComputerPlayer.__init__(self)
        random.seed()



    def select_jumps(self, jumps_list):
        """ Pick the best jump move in list of jumps """
        
        # If only one jump available, there is no choice to make
        if len(jumps_list) == 1:
            return ('jump', jumps_list[0])

        # Prefer jumping more checkers to fewer
        max_jumps = max([len(jumps) for jumps in jumps_list])
        for jumps in jumps_list:
            long_jumps = []
            if len(jumps) == max_jumps:
                long_jumps.append(jumps)

        if len(long_jumps) == 1:
            return ('jump', long_jumps[0])

        # Add code to avoid leaving checker in vulnerable position
        return ('jump', random.choice(long_jumps))


    def select_move(self, moves_list):
        """ Select best move in list """

        # If only one move available, there is no choice to make
        if len(moves_list) == 1:
            return ('move', moves_list[0])

        for move in moves_list:
            # Get the checker that could be moved
            ch = self.checkerboard.get_checker(move[0])

            # If checker can become a king, move it
            if not ch.king and (move[1][0] in (0,7)):
                return ('move', move)

            # If checker is vulnerable to being jumped, move it or block the jump
            

            # Avoid moving into a position to be jumped

            # Target open squares in opponent's home row

            # Move towards center of board to "control the center"

            # Delay moving checkers from home row


    def evaluate_board(self):
        """ Evaluate the checkerboard, to determine next move """

        jumps_list = self.list_jumps()
        if jumps_list:
            return select_jumps(jumps_list)

        moves_list = self.list_moves()
        if moves_list:
            return select_move(moves_list)

        return ('surrender',)


    def play(self):
        """ Determine action in game of checkers """

        evaluation = self.evaluate_board()
        if evaluation[0] == 'jump':
            self.jump_checkers(evaluation[1])
            print("Jump move completed")

        elif evaluation[0] == 'move':
            self.move_checker(evaluation[1])
            print("Move completed")

        else:
            print("I surrender")

        return


