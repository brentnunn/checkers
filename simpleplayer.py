
import functools
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


    @staticmethod
    @functools.lru_cache(maxsize=32)
    def get_neighboring_checkers(square):
        """ Get checkers next to square.
            Squares are stored in a dictionary, keyed on 'ne' for northeast,
            'nw' for northwest, 'se' for southeast, and 'sw' for southwest.
            Normal, not crowned, black checkers move towards the north.
            White checkers move towards the south. """

        return {'ne':self.checkerboard.get_checker(square[0]-1, square[1]-1),
                'nw':self.checkerboard.get_checker(square[0]-1, square[1]+1),
                'se':self.checkerboard.get_checker(square[0]+1, square[1]-1),
                'sw':self.checkerboard.get_checker(square[0]+1, square[1]+1)}


    def checker_vulnerable(self, checker, square=None):
        """ Determine if checker is vulnerable to being jumped """

        if square == None:
            square = checker.position

        # Checkers are not vulnerable if located on one edge of the board
        if (square[0] == 0 or square[0] == 7 or
            square[1] == 0 or square[1] == 7 )
            return False

        # Get neighboring squares so we can check for opponent pieces
        neighbors = get_neighboring_checkers(square)

        if checker.color == 'black':
            if (neighbors['ne'] and neighbors['ne'].color == 'white' and
                (not neighbors['sw'] or neighbors['sw'] == checker)):
                return True
            if (neighbors['nw'] and neighbors['nw'].color == 'white' and
                (not neighbors['se'] or neighbors['se'] == checker)):
                return True
            if (neighbors['se'] and neighbors['se'].color == 'white' and
                neighbors['se'].king and 
                (not neighbors['nw'] or neighbors['nw'] == checker)):
                return True
            if (neighbors['sw'] and neighbors['sw'].color == 'white' and
                neighbors['sw'].king and 
                (not neighbors['ne'] or neighbors['ne'] == checker)):
                return True
            
        else:   # checker.color == 'white'
            if (neighbors['se'] and neighbors['se'].color == 'black' and
                (not neighbors['nw'] or neighbors['nw'] == checker)):
                return True
            if (neighbors['sw'] and neighbors['sw'].color == 'black' and
                (not neighbors['ne'] or neighbors['ne'] == checker)):
                return True
            if (neighbors['ne'] and neighbors['ne'].color == 'black' and
                neighbors['ne'].king and 
                (not neighbors['sw'] or neighbors['sw'] == checker)):
                return True
            if (neighbors['nw'] and neighbors['nw'].color == 'black' and
                neighbors['nw'].king and 
                (not neighbors['se'] or neighbors['se'] == checker)):
                return True

        return False


    def get_open_king_squares(color):
        """ Get open squares from opponent's home row """

        if color == 'black':
            row = 0
            starting_column = 0
        else:
            row = 7
            starting_column = 1

        open_squares = []
        for column in range(starting_column, starting_column + 7, 2):
            if self.checkerboard.get_checker((row, column)) == None:
                open_squares.append((row, column))


    def select_move(self, moves_list):
        """ Select best move in list """

        # If only one move available, there is no choice to make
        if len(moves_list) == 1:
            return ('move', moves_list[0])

        # Any checkers in position to be crowned?
        for move in moves_list:
            # Get the checker that could be moved
            ch = self.checkerboard.get_checker(move[0])

            # If checker can become a king, move it
            if not ch.king and (move[1][0] in (0,7)):
                return ('move', move)

        # Any checkers in danger of being jumped?
        for move in moves_list:
            # Get the checker that could be moved
            ch = self.checkerboard.get_checker(move[0])

            # If checker is vulnerable to being jumped, move it
            #   unless moving it still leaves it vulnerable to being jumped
            # Later, add ability to block jumps
            if checker_vulnerable(ch) and not checker_vulnerable(ch, move[1]):
                return ('move', move)

        # Bias towards moving checkers closer to being crowned
        for move in moves_list:
            # Get the checker that could be moved
            # Target open squares in opponent's home row to crown checker
            ch = self.checkerboard.get_checker(move[0])
            if not ch.king:
                if ch.color == 'black' and ch.position[0] == 2:
                    target_squares = get_open_king_squares('white'):
                    for target_square in target_squares:
                        if (target_square[1] == move[1][1] + 1 or
                            target_square[1] == move[1][1] - 1 or
                            target_square[1] == ch.position[1]):
                            if not checker_vulnerable(ch, move[1]):
                                return ('move', move)
                elif ch.color == 'white' and ch.position[0] == 5:
                    target_squares = get_open_king_squares('black'):
                    for target_square in target_squares:
                        if (target_square[1] == move[1][1] + 1 or
                            target_square[1] == move[1][1] - 1 or
                            target_square[1] == ch.position[1]):
                            if not checker_vulnerable(ch, move[1]):
                                return ('move', move)

        # Bias towards moving checkers towards rows opponent's home row,
        #   and towards center columns
        for move in moves_list:
            ch = self.checkerboard.get_checker(move[0])
            if not ch.king:
                if (ch.color == 'black' and ch.position[0] == 3 and
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

                elif ch.color == 'white' and ch.position[0] == 4:
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

        for move in moves_list:
            ch = self.checkerboard.get_checker(move[0])
            if not ch.king:
                if (ch.color == 'black' and ch.position[0] == 4 and
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

                elif ch.color == 'white' and ch.position[0] == 3:
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

        for move in moves_list:
            ch = self.checkerboard.get_checker(move[0])
            if not ch.king:
                if (ch.color == 'black' and ch.position[0] == 5 and
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

                elif ch.color == 'white' and ch.position[0] == 2:
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

        for move in moves_list:
            ch = self.checkerboard.get_checker(move[0])
            if not ch.king:
                if (ch.color == 'black' and ch.position[0] == 6 and
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

                elif ch.color == 'white' and ch.position[0] == 1:
                    move[1][1] in (1, 2, 3, 4, 5, 6)):
                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

        # Move kings towards center of the board
        for move in moves_list:
            ch = self.checkerboard.get_checker(move[0])
            if ch.king:
                if (((ch.position[0][0] < 2 or ch.position[0][0] > 5) and
                     (move[1][0] > 1 or move[1][0] < 6)) or
                    ((ch.position[0][1] < 2 or ch.position[0][1] > 5) and
                     (move[1][1] > 1 or move[1][1] < 6))):

                    if not checker_vulnerable(ch, move[1]):
                        return ('move', move)

        # Delay moving ordinary checkers from home row
        for move in moves_list:
            ch = self.checkerboard.get_checker(move[0])
            if not (ch.position[0] in (0,7) and not ch.king):
                if not checker_vulnerable(ch, move[1]):
                    return ('move', move)


        # Take any valid move that does not lead to being jumped
        for move in moves_list:
            ch = self.checkerboard.get_checker(move[0])
            if not checker_vulnerable(ch, move[1]):
                return ('move', move)

        # Take any move
        return random.choice(moves_list)


    def evaluate_board(self):
        """ Evaluate the checkerboard, to determine next move """

        jumps_list = self.list_jumps()
        if jumps_list:
            return select_jumps(jumps_list)

        moves_list = self.list_moves()
        if moves_list:
            return select_move(moves_list)

        return ('surrender',)




