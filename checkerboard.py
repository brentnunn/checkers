
import square as sq
import checker as ch

class Checkerboard:
    """ A checkerboard for playing checkers.
        The rules of the game are hard coded into the checkerboard
        and its squares """

    def __init__(self, id):
        """ Create dictionary of 32 squares keyed on standard checkers 
            notation, which numbers squares 1 through 32 """
        self.squares = {}

        self.squares[1] = sq.Square(1, 
                                black_move_squares = ((6, 10), (5, None)),
                                home_row = 'black')
        self.squares[2] = sq.Square(2, 
                                black_move_squares = ((7, 11), (6, 9)),
                                home_row = 'black')
        self.squares[3] = sq.Square(3,
                                black_move_squares = ((8, 12), (7, 10)),
                                home_row = 'black')
        self.squares[4] = sq.Square(4,
                                black_move_squares = ((8, 11)),
                                home_row = 'black')
        self.squares[5] = sq.Square(5, 
                                black_move_squares = ((9, 14)),
                                white_move_squares = ((1, None)))
        self.squares[6] = sq.Square(6, 
                                black_move_squares = ((10, 15), (9, 13)),
                                white_move_squares = ((2, None), (1, None)))
        self.squares[7] = sq.Square(7, 
                                black_move_squares = ((11, 16), (10, 14)),
                                white_move_squares = ((3, None), (2, None)))
        self.squares[8] = sq.Square(8, 
                                black_move_squares = ((12, None), (11, 15)),
                                white_move_squares = ((4, None), (3, None)))
        self.squares[9] = sq.Square(9, 
                                black_move_squares = ((14, 18), (13, None)),
                                white_move_squares = ((6, 2), (5, None)))
        self.squares[10] = sq.Square(10, 
                                black_move_squares = ((15, 19), (14, 17)),
                                white_move_squares = ((7, 3), (6, 1)))
        self.squares[11] = sq.Square(11, 
                                black_move_squares = ((16, 20), (15, 18)),
                                white_move_squares = ((8, 4), (7, 2)))
        self.squares[12] = sq.Square(12, 
                                black_move_squares = ((16, 19)),
                                white_move_squares = ((8, 3)))
        self.squares[13] = sq.Square(13, 
                                black_move_squares = ((17, 22)),
                                white_move_squares = ((9, 6)))
        self.squares[14] = sq.Square(14, 
                                black_move_squares = ((18, 23), (17, 21)),
                                white_move_squares = ((10, 7), (9, 5)))
        self.squares[15] = sq.Square(15, 
                                black_move_squares = ((19, 24), (18, 22)),
                                white_move_squares = ((11, 8), (10, 6)))
        self.squares[16] = sq.Square(16, 
                                black_move_squares = ((20, None), (19, 23)),
                                white_move_squares = ((12, None), (11, 7)))
        self.squares[17] = sq.Square(17, 
                                black_move_squares = ((22, 26), (21, None)),
                                white_move_squares = ((14, 10), (13, None)))
        self.squares[18] = sq.Square(18, 
                                black_move_squares = ((23, 27), (22, 25)),
                                white_move_squares = ((15, 11), (14, 9)))
        self.squares[19] = sq.Square(19, 
                                black_move_squares = ((24, 28), (23, 26)),
                                white_move_squares = ((16, 12), (15, 10)))
        self.squares[20] = sq.Square(20, 
                                black_move_squares = ((24, 27)),
                                white_move_squares = ((16, 11)))
        self.squares[21] = sq.Square(21, 
                                black_move_squares = ((25, 30)),
                                white_move_squares = ((17, 14)))
        self.squares[22] = sq.Square(22, 
                                black_move_squares = ((26, 31), (25, 29)),
                                white_move_squares = ((18, 15), (17, 13)))
        self.squares[23] = sq.Square(23, 
                                black_move_squares = ((27, 32), (26, 30)),
                                white_move_squares = ((19, 16), (18, 14)))
        self.squares[24] = sq.Square(24, 
                                black_move_squares = ((29, None), (27, 31)),
                                white_move_squares = ((20, None), (19, 15)))
        self.squares[25] = sq.Square(25, 
                                black_move_squares = ((30, None), (29, None)),
                                white_move_squares = ((22, 18), (21, None)))
        self.squares[26] = sq.Square(26, 
                                black_move_squares = ((31, None), (30, None)),
                                white_move_squares = ((23, 19), (22, 17)))
        self.squares[27] = sq.Square(27, 
                                black_move_squares = ((32, None), (31, None)),
                                white_move_squares = ((24, 20), (23, 18)))
        self.squares[28] = sq.Square(28, 
                                black_move_squares = ((32, None)),
                                white_move_squares = ((24, 19)))
        self.squares[29] = sq.Square(29, 
                                white_move_squares = ((25, 22)),
                                home_row = 'white')
        self.squares[30] = sq.Square(30, 
                                white_move_squares = ((26, 23), (25, 21)),
                                home_row = 'white')
        self.squares[31] = sq.Square(31, 
                                white_move_squares = ((27, 24), (26, 22)),
                                home_row = 'white')
        self.squares[32] = sq.Square(32, 
                                white_move_squares = ((28, None), (27, 23)),
                                home_row = 'white')

        self.black_checkers = []
        self.white_checkers = []


    def setup_new_board(self):
        """ Setup a new board with 12 checkers on each side 
            in initial positions """

        self.black_checkers = [ch.Checker('black', self) for i in range(12)]
        self.white_checkers = [ch.Checker('white', self) for i in range(12)]

        """ Place checkers in starting squares """
        for enum_ch in enumerate(self.black_checkers):
            """ Black checkers start in squares 1 through 12 """
            self.squares[enum_ch[0] + 1].add_checker(enum_ch[1])

        for enum_ch in enumerate(self.white_checkers):
            """ White checkers start in squares 21 through 32 """
            self.squares[enum_ch[0] + 21].add_checker(enum_ch[1])


    def list_all_positions(self):
        """ List positions of all checkers on the board """

        print('Black positions')
        for ch in self.black_checkers:
            # Need to modify Square class to print id by default        
            if ch.king:
                print(ch.square.id, 'king')
            else:
                print(ch.square.id)

        print('White positions')
        for ch in self.white_checkers:
            if ch.king:
                print(ch.square.id, 'king')
            else:
                print(ch.square.id)


    def remove_checker(self, checker):
        """ Remove specified checker from play """
        if checker.square and checker.square.checker == checker:
            checker.square = None
            
        if checker.color == 'black':
            # Break connection to square.
            checker.square.checker = None
            self.black_checkers.pop(checker)
        elif:
            checker.square.checker = None
            self.white_checkers.pop(checker)
        else:
            # Raise error
            pass

