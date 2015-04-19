
import checker as ch

class Square:
    """ One of the 32 squares on a checkerboard that can be occupied 
        by a checker.
        Squares are numbered 1 to 32 according to standard checkers
        notation used to record games in competitions.
        Each square knows its number (id) and the numbers of neighboring
        squares to which checkers can move or jump to.
        Squares know if they are on a home row of one player on which
        the checkers of the opponent are converted to kings. """
    
    def __init__(self, id):
        
        self.id = id
        self.checker = None

        """ Commented out, but leaving in for now
        self.checker = None
        if id in (1, 2, 3, 4):
            self.home_row = 'black'
        elif id in (29, 30, 31, 32):
            self.home_row = 'white'
        else
            self.home_row = None
        """

        if id == 1:
            self.black_moves = ((6, 10), (5, None))
            self.white_moves = (None)
            self.home_row = 'black'
        elif id == 2:
            self.black_moves = ((7, 11), (6, 9))
            self.white_moves = (None)
            self.home_row = 'black'
        elif id == 3:
            self.black_moves = ((8, 12), (7, 10))
            self.white_moves = (None)
            self.home_row = 'black'
        elif id == 4:
            self.black_moves = ((8, 11))
            self.white_moves = (None)
            self.home_row = 'black'
        elif id == 5:
            self.black_moves = ((9, 14))
            self.white_moves = ((1, None))
            self.home_row = None
        elif id == 6:
            self.black_moves = ((10, 15), (9, 13))
            self.white_moves = ((2, None), (1, None))
            self.home_row = None
        elif id == 7:
            self.black_moves = ((11, 16), (10, 14))
            self.white_moves = ((3, None), (2, None))
            self.home_row = None
        elif id == 8:
            self.black_moves = ((12, None), (11, 15))
            self.white_moves = ((4, None), (3, None))
            self.home_row = None
        elif id == 9:
            self.black_moves = ((14, 18), (13, None))
            self.white_moves = ((6, 2), (5, None))
            self.home_row = None
        elif id == 10:
            self.black_moves = ((15, 19), (14, 17))
            self.white_moves = ((7, 3), (6, 1))
            self.home_row = None
        elif id == 11:
            self.black_moves = ((16, 20), (15, 18))
            self.white_moves = ((8, 4), (7, 2))
            self.home_row = None
        elif id == 12:
            self.black_moves = ((16, 19))
            self.white_moves = ((8, 3))
            self.home_row = None
        elif id == 13:
            self.black_moves = ((17, 22))
            self.white_moves = ((9, 6))
            self.home_row = None
        elif id == 14:
            self.black_moves = ((18, 23), (17, 21))
            self.white_moves = ((10, 7), (9, 5))
            self.home_row = None
        elif id == 15:
            self.black_moves = ((19, 24), (18, 22))
            self.white_moves = ((11, 8), (10, 6))
            self.home_row = None
        elif id == 16:
            self.black_moves = ((20, None), (19, 23))
            self.white_moves = ((12, None), (11, 7))
            self.home_row = None
        elif id == 17:
            self.black_moves = ((22, 26), (21, None))
            self.white_moves = ((14, 10), (13, None))
            self.home_row = None
        elif id == 18:
            self.black_moves = ((23, 27), (22, 25))
            self.white_moves = ((15, 11), (14, 9))
            self.home_row = None
        elif id == 19:
            self.black_moves = ((24, 28), (23, 26))
            self.white_moves = ((16, 12), (15, 10))
            self.home_row = None
        elif id == 20:
            self.black_moves = ((24, 27))
            self.white_moves = ((16, 11))
            self.home_row = None
        elif id == 21:
            self.black_moves = ((25, 30))
            self.white_moves = ((17, 14))
            self.home_row = None
        elif id == 22:
            self.black_moves = ((26, 31), (25, 29))
            self.white_moves = ((18, 15), (17, 13))
            self.home_row = None
        elif id == 23:
            self.black_moves = ((27, 232), (26, 30))
            self.white_moves = ((19, 16), (18, 14))
            self.home_row = None
        elif id == 24:
            self.black_moves = ((28, None), (27, 31))
            self.white_moves = ((20, None), (19, 15))
            self.home_row = None
        elif id == 25:
            self.black_moves = ((30, None), (29, None))
            self.white_moves = ((22, 18), (21, None))
            self.home_row = None
        elif id == 26:
            self.black_moves = ((31, None), (30, None))
            self.white_moves = ((23, 19), (22, 17))
            self.home_row = None
        elif id == 27:
            self.black_moves = ((32, None), (31, None))
            self.white_moves = ((24, 20), (23, 18))
            self.home_row = None
        elif id == 28:
            self.black_moves = ((32, None))
            self.white_moves = ((24, 19))
            self.home_row = None
        elif id == 29:
            self.black_moves = (None)
            self.white_moves = ((25, 22))
            self.home_row = 'white'
        elif id == 30:
            self.black_moves = (None)
            self.white_moves = ((26, 23), (25, 21))
            self.home_row = 'white'
        elif id == 31:
            self.black_moves = (None)
            self.white_moves = ((27, 24), (26, 22))
            self.home_row = 'white'
        elif id == 32:
            self.black_moves = (None)
            self.white_moves = ((28, None), (27, 23))
            self.home_row = 'white'
        else:
            """ Raise an error here """
            pass


    
    def add_checker(self, checker):
        """ Add a checker to the current square.
            Inform the checker of its new square. """
        self.checker = checker
        checker.square = self

