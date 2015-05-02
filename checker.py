
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


    def set_square(self, row, column):
            self.position = [row, column]


