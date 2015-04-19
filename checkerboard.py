
import square as sq
import checker as ch

class Checkerboard:
    """ The rules of the game are hard coded into the checkerboard
        and its squares """

    # Generate 12 checkers for each side
    black_checkers = [ch.Checker('black') for i in range(16)]
    white_checkers = [ch.Checker('white') for i in range(16)]

    """ Create dictionary of 32 squares keyed on standard checkers notation, 
        which numbers dark squares 1 through 32 """
    squares = {k: sq.Square() for k in range(1, 33)}

    # Create a checkerboard array, 8 x 8
    # Not sure the array is necessary, but keeping it for now
    checkerboard = [[None]*8 for i in range(8)]

    # Assign dark squares to their checkerboard locations
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

    # Set square attributes based on checkerboard position
    squares[1].black_moves = ((6, 10), (5, None))
    squares[1].white_moves = ((None, None), (None, None))
    squares[1].home_row = 'black'
    squares[1].checker = black_checkers[0]
    black_checkers[0].square = squares[1]

    squares[2].black_move_squares = (7, 6)
    squares[2].black_jump_squares = (11, 9)
    squares[2].home_row = 'black'
    squares[2].checker = black_checkers[1]

    squares[3].black_move_squares = (8, 7)
    squares[3].black_jump_squares = (12, 10)
    squares[3].home_row = 'black'
    squares[3].checker = black_checkers[2]

    squares[4].black_move_squares = (8)
    squares[4].black_jump_squares = (11)
    squares[4].home_row = 'black'





    checkerboard[7, 6] = Square(((6,5),(6,7)), ((5,4)), None, None,
                                 home_row = 'black', checker = black_checkers[0])

    checkerboard[7, 4] = Square(((6,3),(6,5)), ((5,2),(5,6)), None, None,
                                 home_row = 'black', checker = black_checkers[1])

    checkerboard[7, 2] = Square(((6,1),(6,3)), ((5,0),(5,4)), None, None,
                                 home_row = 'black', checker = black_checkers[2])

    checkerboard[7, 0] = Square(((6,1),((5,2)), None, None,
                                 home_row = 'black', checker = black_checkers[3])

    checkerboard[6, 7] = Square(((5,6),((4,5)), ((7,6)), None,
                                 home_row = 'black', checker = black_checkers[4])

    checkerboard[6, 5] = Square(((5,4),(5,6)), ((4,3), (4,7)), ((7,4),(7,6)), None,
                                 home_row = None, checker = black_checkers[5])

    checkerboard[6, 3] = Square(black_checkers[6])

    checkerboard[6, 1] = Square(black_checkers[7])

    checkerboard[5, 6] = Square(black_checkers[8])

    checkerboard[5, 4] = Square(black_checkers[9])

    checkerboard[5, 2] = Square(black_checkers[10])

    checkerboard[5, 0] = Square(black_checkers[11])



