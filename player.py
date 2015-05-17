
import logging
import checkerboard as cb
import checker as ch

logger = logging.getLogger(__name__)

class Player:

    next_id = 1

    def __init__(self):
        self.name = None
        self.wins = 0
        self.losses = 0
        self.draws = 0

        self.id = Player.next_id
        Player.next_id += 1

        self.checkerboard = None
        self.checkers = []



