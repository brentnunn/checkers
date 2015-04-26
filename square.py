
import checker as ch

class Square:
    """ One of the 32 squares on a checkerboard that can be occupied 
        by a checker.
        Squares are numbered 1 to 32 according to standard checkers
        notation used to record games in competitions.
        Each square knows its number (id) and the numbers of neighboring
        squares to which checkers can move to or jump to.
        Squares know if they are on a home row of one player on which
        the checkers of the opponent are converted to kings. """
    
    def __init__(self, id, black_move_squares=None, 
                 white_move_squares=None, home_row=None):
        """ Possible moves are encoded as a tuple of tuples.
            Each inner tuple consists of the identities of 
            2 squares: (move_square, jump_square).
            If the move square is open, then a checker can move there.
            If the move square is occupied by an opponent's piece, 
            then a checker can jump to the jump square, if it is open. 
            """
        self.id = id
        self.black_move_squares = black_move_squares
        self.white_move_squares = white_move_squares
        self.home_row = home_row
        self.checker = None

    
    def add_checker(self, checker):
        """ Add a checker to the current square.
            Inform the checker of its new square. """
        self.checker = checker
        checker.square = self


    def remove_checker(self, checker):
        """ Remove connection between a checker and this square """
        checker.square = None
        self.checker = None


    """
    def get_moves(self):
        # Return the moves that can be made by the checker on this square

        if self.checker.king:
            return black_neighboring_squares + white_neighboring_squares
        else:
            if self.checker.color = 'black':
                return self.black_neighboring_squares
            else:
                return self.white_neighboring_squares
    """


