
import checkerboard as cb

class Checker:

    def __init__(self, color, checkerboard):
        self.color = color
        self.king = False
        self.checkerboard = checkerboard
        self.position = []


    def __str__(self):
        if self.king:
            return ' ' + self.color[0] + 'k '
        else:
            return ' ' + self.color[0] + '  '


    @staticmethod
    def get_black_squares(row, column):
        """ Get squares that a black checker at row & column could move
            or jump to.  Neighboring squares are returned as a tuple 
            with 2 values: position 0 is the move square, position 1
            is the jump square. """
        
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
    def get_white_squares(row, column):
        """ Get squares that a white checker at row & column could move
            or jump to.  Neighboring squares are returned as a tuple 
            with 2 values: position 0 is the move square, position 1
            is the jump square. """
        
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
           


