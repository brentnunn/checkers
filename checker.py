
import square as sq

class Checker:

    def __init__(self, color):
        self.color = color
        self.square = None
        self.king = False


    def get_neighboring_squares(self, square):
        """ What are the possible moves from current position? """
        if king:
            return(square.black_neighboring_squares + 
                   square.white_neighboring_squares)
        else:
            if color == 'black':
                return square.black_neighboring_squares
            else:
                return square.white_neighboring_squares


    def check_for_jump(self):
        """ Can current checker make a jump in any direction? """

        for neighbors in self.get_neighboring_squares(self.square):
            """ Check for opponent in neighboring square and that the
                square on other side of opponent's checker is empty """
            if (neighbors[0].checker.color != self.color
                and neighbors[1].checker == None):

                return True

        return False

 
    def list_moves(self):
        """ List non-jump moves from the current square.
            Each move is a list encoded as the starting square followed
            by the ending square. """

        moves = []

        # Neighboring squares without a checker are possible moves
        for neighbors in self.get_neighboring_squares(self.square):
            if neighbors[0].checker == None:
                moves.append(self.square, neighbors[0])

        return moves


    def build_jump_lists(self, square):
        """ Build lists of possible jumps """
        jump_list.append(square)
        terminus = True

        for neighbors in self.get_neighboring_squares(self.square):
            if (neighbors[0].checker.color != self.color and
                neighbors[0].checker not in jump_list and 
                (neighbors[1].checker == None or
                # Account for possibly jumping in a circle
                #  Maybe use "... in (None, self.checker) ?"
                neighbors[1].checker == self.checker)):

                # Jumps available, we are not at the end of a jump list
                terminus = False
                # Keep track of checkers jumped
                jumped_checkers.append(neighbors[0].checker)
                # Recursively walk the tree of possible jumps
                build_jump_lists(neighbors[1].square)

        if terminus:
            """ If this square did not allow any jumps,
                then one list of possible jumps is complete. """
            list_of_jump_lists.append(jump_list)

        jump_list.pop()
        jumped_checkers.pop()

        return


    def list_jump_squares(self):
        """ This routine returns a list of lists.
            Each inner list represents one set of jumps terminating at
            a square from which no further jumps are available. """
        
        jump_list = []
        list_of_jump_lists = []

        # Track jumped checkers so we don't try to jump them twice
        jumped_checkers = []

        """ Check for jumps around starting position """
        for neighbors in self.get_neighboring_squares(self.square):
            if (neighbors[0].checker.color != self.color and 
                neighbors[1].checker == None):

                jump_list.append(self)
                jumped_checkers.append(neighbors[0].checker)
                build_jump_lists(neighbors[1].square)

        return list_of_jump_lists


    def move(self, square_id):
        """ Break connection to old square.
            Establish connection to new square.
            Become a king, if appropriate. """

        """ NEEDED: Translate square_id to identity of square in Python """
        self.square.checker = None
        square.add_checker(self)
        if (square.home_row and square.home_row != self.color and
            not self.king):
            self.king = True


    def jump_to_square(self, square):
        pass


    def jump(self, square):
        pass

