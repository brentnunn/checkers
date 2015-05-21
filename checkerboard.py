
import logging
import checker as ch

logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

class Checkerboard:
    """ A checkerboard for playing checkers """

    def __init__(self):
        """ Create a 2 dimensional array representing checkerboard 
            squares """
        self.squares = [[None for j in range(8)] for i in range(8)]

        self.black_checkers = []
        self.white_checkers = []

        logger.info('Initialized checkerboard {}'.format(self))


    def dark_square(self, square):
        """ True if this is a dark square, a valid location 
            for a checker """

        logger.debug('dark_square({})'.format(square))

        row, column = square
        return (row + column) % 2 != 0


    def print_board(self):
        """ Print the contents of the checkerboard """

        print()

        for row in range(8):
            for column in range(8):
                if self.squares[row][column]:
                    print(self.squares[row][column], end='')
                else:
                    if self.dark_square((row, column)):
                        print(' __ ', end='')
                    else:
                        print(' .  ', end='')
            print()
        print()


    def place_checker(self, square, checker):
        """ Place checker on square """

        logger.debug('place_checker({}, {})'.format(square, checker))

        row, column = square
        self.squares[row][column] = checker
        checker.position = (row, column)


    def get_checker(self, square):
        """ Return reference to the checker at square """

        logger.debug('get_checker({})'.format(square))

        row, column = square
        return self.squares[row][column]


    def remove_checker(self, square):
        """ Remove checker from the board """

        logger.debug('remove_checker({})'.format(square))

        checker = self.get_checker(square)
        logger.debug('remove_checker(): checker={}'.format(checker))

        row, column = square
        self.squares[row][column] = None

        if checker.color == 'black':
            self.black_checkers.remove(checker)
        else:
            self.white_checkers.remove(checker)


    def setup_new_board(self):
        """ Setup a new board with 12 checkers on each side 
            in starting positions """

        logger.info('setup_new_board()')

        self.black_checkers = [ch.Checker('black', self) for i in range(12)]
        self.white_checkers = [ch.Checker('white', self) for i in range(12)]

        """ Place checkers in starting squares """
        i = 0
        for row in range(3):
            for column in range(8):
                if self.dark_square((row, column)):
                    self.place_checker((row, column), self.white_checkers[i])
                    i += 1

        i = 0
        for row in range(5, 8):
            for column in range(8):
                if self.dark_square((row, column)):
                    self.place_checker((row, column), self.black_checkers[i])
                    i += 1


