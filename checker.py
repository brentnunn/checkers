
import checkerboard as cb

class Checker:

    def __init__(self, color, checkerboard):
        self.color = color
        self.king = False
        self.checkerboard = checkerboard
        self.position = []
        self._jumped_checkers = []
        self._jump_chain = []
        self._list_of_jump_chains = []


    def __str__(self):
        if self.king:
            return ' ' + self.color[0] + 'k '
        else:
            return ' ' + self.color[0] + '  '


    @staticmethod
    def get_black_move_squares(square):
        """ Get neighboring squares that a black checker at square could
            move or jump to.  Neighboring squares are returned as a tuple 
            with 2 values: position 0 is the move square, position 1
            is the jump square. """
        
        row, column = square
        if row == 0:
            # No moves or jumps to calculate
            return (None, )

        nw = [None, None]
        ne = [None, None]

        # Calculate black move squares
        if column > 0:
            nw[0] = (row - 1, column - 1)
        if column < 7:
            ne[0] = (row - 1, column + 1)

        if row == 1:
            return (nw, ne)

        # Calculate black jump squares
        if column > 1:
            nw[1] = (row - 2, column - 2)
        if column < 6:
            ne[1] = (row - 2, column + 2)

        return (nw, ne)


    @staticmethod
    def get_white_move_squares(square):
        """ Get neighboring squares that a white checker at square could
            move or jump to.  Neighboring squares are returned as a tuple 
            with 2 values: position 0 is the move square, position 1
            is the jump square. """
        
        row, column = square
        if row == 7:
            # No moves or jumps to calculate
            return (None, )

        sw = [None, None]
        se = [None, None]

        # Calculate white move squares
        if column > 0:
            sw[0] = (row + 1, column - 1)
        if column < 7:
            se[0] = (row + 1, column + 1)

        if row == 6:
            return (sw, se)

        # Calculate white jump squares
        if column > 1:
            sw[1] = (row + 2, column - 2)
        if column < 6:
            se[1] = (row + 2, column + 2)

        return (sw, se)
           

    def get_checker(self, square):
        """ Return reference to the checker at square """
        row, column = square
        return self.checkerboard.squares[row][column]


    def get_neighboring_squares(self, square=None):
        """ Return the neighboring squares to which a checker might move
            or jump to. """

        if square == None:
            square = self.position

        if self.king:
            return (self.get_black_move_squares(self.position) + 
                    self.get_white_move_squares(self.position))
        else:
            if self.color == 'black':
                return self.get_black_move_squares(self.position)
            else:
                return self.get_white_move_squares(self.position)


    def list_moves(self):
        """ List non-jump moves from the current square.
            Each move is a list encoded as the starting square followed
            by the ending square. """

        moves = []

        # Neighboring squares without a checker are possible moves
        for move_square, jump_square in self.get_neighboring_squares():
            if self.get_checker(move_square) == None:
                moves.append((self.position, move_square))

        return moves


    def _change_square(self, square):
        """ Change checker's square """
        new_row, new_column = square

        # Remove reference to this checker from old position
        self.checkerboard.squares[self.position[0]][self.position[1]] = None

        # Place checker in new position
        self.checkerboard.squares[new_row][new_column] = self
        self.position = [new_row, new_column]


    def move(self, square):
        """ Move checker to square """

        # Verify we are moving to an empty neighboring square
        if (square in [sq[0] for sq in self.get_neighboring_squares()] and
            self.get_checker(square) == None):
            
            self._change_square(square)

        else:
            # raise Illegal Move error
            print("Invalid move from", self.position, "to", square)


    def check_for_jump(self):
        """ Return true if checker has a jump move available """

        for move_square, jump_square in self.get_neighboring_squares():
            if jump_square:
                move_square_checker = self.get_checker(move_square)
                jump_square_checker = self.get_checker(jump_square)

                if (isinstance(move_square_checker, Checker) and
                    move_square_checker.color != self.color and
                    jump_square_checker == None):

                    return True

        return False


    def _add_jump_square(self, square):
        """ Add a jump square to a chain of jumps """
        self._jump_chain.append(square)

        # Check for more jumps from new position
        # will need another for loop here, checking square's neighbors

        # If no more jumps available, we are at the end of a jump chain
        self._list_of_jump_chains.append(self._jump_chain)
        self._jump_chain.pop()
        self._jumped_checkers.pop()
        return


    def list_jumps(self):
        """ List all possible jumps from checker's position """

        print("list_jumps: position = ", this.position)

        self._list_of_jump_chains = []
        # Each jump chain begins with checker's starting position
        self._jump_chain = [this.position]

        for neighbors in self.get_neighboring_squares():
            if (neighbors[1] and
                # Verify jump landing square is empty
                (self.get_checker(neighbors[1]) == None or
                # Allow for possibly jumping in a circle back to start
                self.get_checker(neighbors[1]) == self) and
                # Is there an opponent's checker to jump over?
                self.get_checker(neighbors[0]) and
                self.get_checker(neighbors[0]).color != self.color and
                # Prevent trying to jump the same checker twice
                self.get_checker(neighbors[0]) not in self._jumped_checkers):

                # Keep track of jumped checkers
                self._jumped_checkers = [self.get_checker(neighbors[0])]
                #self._jumped_checkers.append(self.get_checker(neighbors[0]))

                # Add target squares to the jump chain
                self._add_jump_square(neighbors[1])

                print("list_jumps: Jump checker = ", neighbors[0])
                print("list_jumps: Jump to square = ", neighbors[1])

                #self._jump_chain = [self.position, ]

        print("list_jumps: _jumped_checkers = ", self._jumped_checkers)
        print("list_jumps: _list_of_jump_chains = ", self._list_of_jump_chains)

        return self._list_of_jump_chains


    def jump(self, square):
        """ Checker jumps to square """

        # Verify valid jump
        for jumped_square, jump_to_square in self.get_neighboring_squares():
            if jump_to_square == square:
                jumped_square_checker = self.get_checker(jumped_square)
                jump_to_square_checker = self.get_checker(jump_to_square)

                if (isinstance(jumped_square_checker, Checker) and
                    jumped_square_checker.color != self.color and
                    jump_to_square_checker == None):

                    # Valid jump, remove jumped checker
                    row, column = jumped_square
                    self.checkerboard.remove_checker(row, column)

                    self._change_square(jump_to_square)

                    return

        # Invalid jump request
        print("Invalid jump from", self.position, "to", jumped_square)




#    def build_jump_chains(self, jump):
#        """ Build lists of possible jumps """
#        print("build_jump_chains: jump =", jump)#
#
#        self._jump_chain.append(jump)
#        new_square = self.checkerboard.squares[jump[1]]
#        print("build_jump_chains: new_square =", new_square.id)
#        terminus = True#
#
#        print("get_neighboring_squares(new_square) = ", self.get_neighboring_squares(new_square))
#        for neighbors in self.get_neighboring_squares(new_square):
#            print("build_jump_chains: neighbors =", neighbors)
#
#            if (neighbors[1] and
#                (self.get_checker(neighbors[1]) == None or
#                # Allow for possibly jumping in a circle back to start
#                self.get_checker(neighbors[1]) == self) and
#                self.get_checker(neighbors[0]) and
#                self.get_checker(neighbors[0]).color != self.color and
#                # Prevent trying to jump the same checker twice
#                self.get_checker(neighbors[0]) not in self._jumped_checkers):#
#
#                # Jumps available, we are not at the end of a jump list
#                terminus = False
#
#                print("build_jump_chains: terminus =", terminus)
#
#                # Keep track of checkers jumped
#                self._jumped_checkers.append(self.get_checker(neighbors[0]))
#
#                print("build_jump_chains: _jumped_checkers before recursive call =", self._jumped_checkers)
#
#                # Recursively walk the tree of possible jumps
#                self.build_jump_chains(neighbors)
#
#                print("build_jump_chains: _jumped_checkers after recursive call =", self._jumped_checkers)
#                print("build_jump_chains: _jump_chain after recursive call =", self._jump_chain)
#
#
#        if terminus:
#            """ If this square did not allow any further jumps,
#                then one chain of possible jumps is complete. """
#            print("build_jump_chains: terminus if test ==", terminus)
#
#            self._list_of_jump_chains.append(self._jump_chain)
#        else:
#            self._jump_chain.pop()
#            self._jumped_checkers.pop()
#
#        return

