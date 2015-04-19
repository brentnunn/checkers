
import square as sq
import checker as ch

class Checkerboard:
    """ A checkerboard for playing checkers.
        The rules of the game are hard coded into the checkerboard
        and its squares """

    def __init__(self, id):
        """ Create dictionary of 32 squares keyed on standard checkers 
            notation, which numbers dark squares 1 through 32 """
        squares = {k: sq.Square(k) for k in range(1, 33)}

        """ Generate 12 checkers for each side """
        black_checkers = [ch.Checker('black') for i in range(12)]
        white_checkers = [ch.Checker('white') for i in range(12)]

        """ Place checkers in starting positions """
        for enum_ch in enumerate(black_checkers):
            squares[enum_ch[0] + 1].add_checker(enum_ch(1))

        for enum_ch in enumerate(white_checkers):
            squares[enum_ch[0] + 21].add_checker(enum_ch(1))


        """ Create a checkerboard array, 8 x 8
            Not sure the array is necessary, but keeping it for now """
        checkerboard = [[None]*8 for i in range(8)]

        """ Assign squares to their checkerboard locations """
        checkerboard[7,6] = squares[1]
        checkerboard[7,4] = squares[2]
        checkerboard[7,2] = squares[3]
        checkerboard[7,0] = squares[4]
        checkerboard[6,7] = squares[5]
        checkerboard[6,5] = squares[6]
        checkerboard[6,3] = squares[7]
        checkerboard[6,1] = squares[8]
        checkerboard[5,6] = squares[9]
        checkerboard[5,4] = squares[10]
        checkerboard[5,2] = squares[11]
        checkerboard[5,0] = squares[12]
        checkerboard[4,7] = squares[13]
        checkerboard[4,5] = squares[14]
        checkerboard[4,3] = squares[15]
        checkerboard[4,1] = squares[16]
        checkerboard[3,6] = squares[17]
        checkerboard[3,4] = squares[18]
        checkerboard[3,2] = squares[19]
        checkerboard[3,0] = squares[20]
        checkerboard[2,7] = squares[21]
        checkerboard[2,5] = squares[22]
        checkerboard[2,3] = squares[23]
        checkerboard[2,1] = squares[24]
        checkerboard[1,6] = squares[25]
        checkerboard[1,4] = squares[26]
        checkerboard[1,2] = squares[27]
        checkerboard[1,0] = squares[28]
        checkerboard[0,7] = squares[29]
        checkerboard[0,5] = squares[30]
        checkerboard[0,3] = squares[31]
        checkerboard[0,1] = squares[32]








