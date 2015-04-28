
import square as sq

class Checker:

    def __init__(self, color, checkerboard):
        self.color = color
        self.checkerboard = checkerboard
        self.square = None
        self.king = False
        _jump_chain = []
        _list_of_jump_chains = []
        _jumped_checkers = []


        # REFACTOR: Return square, not square id
    def get_neighboring_squares(self, square=None):
        """ What are the possible moves from current position? """
        if square == None:
            square = self.square

        if self.king:
            return(square.black_move_squares + 
                   square.white_move_squares)
        else:
            if self.color == 'black':
                return self.square.black_move_squares
            else:
                return self.square.white_move_squares


    def get_checker(self, square_id):
        """ Find checker associated with square_id """
        return self.checkerboard.squares[square_id].checker


    def check_for_jump(self):
        """ Can current checker make a jump in any direction? """

        for neighbors in self.get_neighboring_squares():
            """ Check for opponent in neighboring square and that the
                square on other side of opponent's checker is empty """
            if (self.get_checker(neighbors[0]) and
                self.get_checker(neighbors[0]).color != self.color and
                self.get_checker(neighbors[1]) == None):

                return True

        return False

 
    def list_moves(self):
        """ List non-jump moves from the current square.
            Each move is a list encoded as the starting square followed
            by the ending square. """

        moves = []

        # Neighboring squares without a checker are possible moves
        for neighbors in self.get_neighboring_squares():
            if self.get_checker(neighbors[0]) == None:
                moves.append(self.square, neighbors[0])

        return moves


    def build_jump_chains(self, jump):
        """ Build lists of possible jumps """
        self._jump_chain.append(jump)
        new_square = self.checkerboard.squares[jump[1]]
        terminus = True

        for neighbors in self.get_neighboring_squares(new_square):
            if (neighbors[1] and
                (self.get_checker(neighbors[1]) == None or
                # Allow for possibly jumping in a circle back to start
                self.get_checker(neighbors[1]) == self.checker) and
                self.get_checker(neighbors[0]) and
                self.get_checker(neighbors[0]).color != self.color and
                # Prevent trying to jump the same checker twice
                self.get_checker(neighbors[0]) not in self._jumped_checkers):

                # Jumps available, we are not at the end of a jump list
                terminus = False
                # Keep track of checkers jumped
                self._jumped_checkers.append(neighbors[0].checker)
                # Recursively walk the tree of possible jumps
                build_jump_chains(neighbors)

        if terminus:
            """ If this square did not allow any further jumps,
                then one chain of possible jumps is complete. """
            self._list_of_jump_chains.append(self._jump_chain)

        self._jump_list.pop()
        self._jumped_checkers.pop()

        return


    def list_jump_squares(self):
        """ This routine returns a list of lists.
            Each inner list, a jump chain, represents one set of jumps 
            terminating at a square from which no further jumps are 
            available. 
            The first entry in the jump chain is the starting square_id.
            Subsequent entries in the jump chain are tuples consisting
            of the checker jumped and the square_id jumped to. """
        
        self._list_of_jump_chains = []
        self._jumped_checkers = []

        """ Check for jumps around starting position """
        for neighbors in self.get_neighboring_squares():
            if (self.get_checker(neighbors[0]) and
                self.get_checker(neighbors[0]).color != self.color and 
                self.neighbors[1] and
                self.get_checker(neighbors[1]) == None):

                # Starting a new jump chain
                self._jump_chain = []
                # Jump chains begin with the starting square_id
                self._jump_chain.append(self.square.square_id)
                jumped_checker = get_checker(neighbors[0])
                self._jumped_checkers.append(jumped_checker)
                self.build_jump_chains(neighbors)

        return self._list_of_jump_chains


    def move(self, square_id):
        """ Move checker to a new square.
            Break connection to old square.
            Establish connection to new square.
            Become a king, if appropriate. """

        # Break connection to old square.
        self.square.checker = None
        # Establish connection to new square.
        self.checkerboard.squares[square_id].add_checker(self)
        #square.add_checker(self)
        if (self.square.home_row and 
            self.square.home_row != self.color 
            and not self.king):
            self.king = True


    def jump(self, square_ids):
        """ Jump through the list of square ids, removing jumped
            checkers from the checkerboard. """

        jump_list = square_ids
        # Verify starting position is current checker's square
        square_id = jump_list.pop(0)
        if square_id != self.square.square_id:
            # Raise error, jump list must start with current position
            pass

        for jump in jump_list:
            self.jump_checker(jump[0])
            self.move(jump[1])


    def jump_checker(self, square_id):
        """ Jump checker at specified square id """
        self.checkerboard.remove_checker(get_checker(square_id))

