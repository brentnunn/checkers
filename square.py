
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
    
    def __init__(self, id, black_moves=None, white_moves=None, 
                 home_row=None):
        """ Possible moves are encoded as a tuple of tuples.
            Each inner tuple consists of the identities of 
            2 squares: (move_square, jump_square).
            If the move square is open, then a checker can move there.
            If the move square is occupied by an opponent's piece, 
            then a checker can go to the jump square, if it is open. """
        self.id = id
        self.black_moves = black_moves
        self.white_moves = white_moves
        self.home_row = home_row
        self.checker = None

    
    def add_checker(self, checker):
        """ Add a checker to the current square.
            Inform the checker of its new square. """
        self.checker = checker
        checker.square = self


    def get_checker(self):
        return self.checker


    def list_black_move_squares(self):
        pass


    def list_black_jump_squares(self):
        pass

        
    def list_white_move_squares(self):
        pass


    def list_white_jump_squares(self):
        pass
