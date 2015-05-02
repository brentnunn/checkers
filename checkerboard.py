
import checker as ch

class Checkerboard:
    """ A checkerboard for playing checkers.
        The rules of the game are hard coded into the checkerboard
        and its squares """

    def __init__(self):
        """ Create a 2 dimensional array representing checkerboard 
            squares """
        self.squares = [[None for j in range(8)] for i in range(8)]

        self.black_checkers = []
        self.white_checkers = []


    def print_board(self):
        """ Print the contents of the checkerboard """
        print()

        for row in range(8):
            for column in range(8):
                if self.squares[row][column]:
                    print(self.squares[row][column], end='')
                else:
                    if self.dark_square(row, column):
                        print(' __ ', end='')
                    else:
                        print(' .  ', end='')
            print()

        print()


    def dark_square(self, row, column):
        """ True if this is a dark square, a valid location 
            for a checker """
        return (row + column) % 2 != 0


    def place_checker(self, row, column, checker):
        """ Place checker on square """
        self.squares[row][column] = checker
        checker.position = [row, column]


    def setup_new_board(self):
        """ Setup a new board with 12 checkers on each side 
            in starting positions """

        self.black_checkers = [ch.Checker('black', self) for i in range(12)]
        self.white_checkers = [ch.Checker('white', self) for i in range(12)]

        """ Place checkers in starting squares """
        i = 0
        for row in range(3):
            for column in range(8):
                if self.dark_square(row, column):
                    self.squares[row][column] = self.white_checkers[i]
                    i += 1

        i = 0
        for row in range(5, 8):
            for column in range(8):
                if self.dark_square(row, column):
                    #self.squares[row][column] = self.black_checkers[i]
                    self.place_checker(row, column, self.black_checkers[i])
                    i += 1



    """
    def remove_checker(self, checker):
        # Remove specified checker from play
        if checker.square and checker.square.checker == checker:
            checker.square.checker == None

        if checker.color == 'black':
            # Break connection to square.
            self.black_checkers.pop(checker)
        else:
            self.white_checkers.pop(checker)
    """

