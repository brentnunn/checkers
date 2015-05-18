
import unittest
import checkerboard as cb
import checker as ch
import random


class testChecker(unittest.TestCase):
    """ Tests for the Checker class """


    def test_init(self):
        cb1 = cb.Checkerboard()
        ch1 = ch.Checker('black', cb1)

        with self.subTest('Testing checker __init__'):
            self.assertEqual(ch1.color, 'black')
            self.assertEqual(ch1.checkerboard, cb1)
            self.assertEqual(ch1.position, ())

    
    def test_get_black_move_squares(self):
        with self.subTest('Testing get_black_move_squares'):
            move_squares = ch.Checker.get_black_move_squares((0,1))
            self.assertEqual(move_squares, (None, None))
            move_squares = ch.Checker.get_black_move_squares((0,7))
            self.assertEqual(move_squares, (None, None))
            move_squares = ch.Checker.get_black_move_squares((1,0))
            self.assertEqual(move_squares, ([None, None], [(0, 1), None]))
            move_squares = ch.Checker.get_black_move_squares((1,2))
            self.assertEqual(move_squares, ([(0, 1), None], [(0, 3), None]))
            move_squares = ch.Checker.get_black_move_squares((1,6))
            self.assertEqual(move_squares, ([(0, 5), None], [(0, 7), None]))
            move_squares = ch.Checker.get_black_move_squares((2,1))
            self.assertEqual(move_squares, ([(1, 0), None], [(1, 2), (0, 3)]))
            move_squares = ch.Checker.get_black_move_squares((2,3))
            self.assertEqual(move_squares, ([(1, 2), (0, 1)], [(1, 4), (0, 5)]))
            move_squares = ch.Checker.get_black_move_squares((2,5))
            self.assertEqual(move_squares, ([(1, 4), (0, 3)], [(1, 6), (0, 7)]))
            move_squares = ch.Checker.get_black_move_squares((2,7))
            self.assertEqual(move_squares, ([(1, 6), (0, 5)], [None, None]))
            move_squares = ch.Checker.get_black_move_squares((7,0))
            self.assertEqual(move_squares, ([None, None], [(6, 1), (5, 2)]))
            move_squares = ch.Checker.get_black_move_squares((7,2))
            self.assertEqual(move_squares, ([(6, 1), (5, 0)], [(6, 3), (5, 4)]))
            move_squares = ch.Checker.get_black_move_squares((7,6))
            self.assertEqual(move_squares, ([(6, 5), (5, 4)], [(6, 7), None]))
    

    
    def test_get_white_move_squares(self):
        with self.subTest('Testing get_white_move_squares'):
            move_squares = ch.Checker.get_white_move_squares((0,1))
            self.assertEqual(move_squares, ([(1, 0), None], [(1, 2), (2, 3)]))
            move_squares = ch.Checker.get_white_move_squares((0,7))
            self.assertEqual(move_squares, ([(1, 6), (2, 5)], [None, None]))
            move_squares = ch.Checker.get_white_move_squares((1,0))
            self.assertEqual(move_squares, ([None, None], [(2, 1), (3, 2)]))
            move_squares = ch.Checker.get_white_move_squares((1,2))
            self.assertEqual(move_squares, ([(2, 1), (3, 0)], [(2, 3), (3, 4)]))
            move_squares = ch.Checker.get_white_move_squares((1,6))
            self.assertEqual(move_squares, ([(2, 5), (3, 4)], [(2, 7), None]))
            move_squares = ch.Checker.get_white_move_squares((2,1))
            self.assertEqual(move_squares, ([(3, 0), None], [(3, 2), (4, 3)]))
            move_squares = ch.Checker.get_white_move_squares((2,3))
            self.assertEqual(move_squares, ([(3, 2), (4, 1)], [(3, 4), (4, 5)]))
            move_squares = ch.Checker.get_white_move_squares((2,5))
            self.assertEqual(move_squares, ([(3, 4), (4, 3)], [(3, 6), (4, 7)]))
            move_squares = ch.Checker.get_white_move_squares((2,7))
            self.assertEqual(move_squares, ([(3, 6), (4, 5)], [None, None]))
            move_squares = ch.Checker.get_white_move_squares((7,0))
            self.assertEqual(move_squares, (None, None))
            move_squares = ch.Checker.get_white_move_squares((7,6))
            self.assertEqual(move_squares, (None, None))
    


    def test_get_checker(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        random.seed()

        with self.subTest('Testing get_checker'):
            ch1 = random.choice(cb1.black_checkers)
            ch2 = ch1.get_checker((5,2))
            self.assertEqual(ch2, cb1.squares[5][2])


    def test_get_move_squares(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        with self.subTest('Testing get_move_squares for black checker'):
            ch1 = cb1.get_checker((5,2))
            self.assertTrue(ch1.color == 'black')
            moves_list1 = ch1.get_move_squares()
            moves_list2 = ch1.get_move_squares(ch1.position)
            self.assertEqual(moves_list1, moves_list2)
            self.assertTrue(len(moves_list1) == 2)
            self.assertEqual(moves_list1, ([(4, 1), (3, 0)], [(4, 3), (3, 4)]))

        with self.subTest('Testing get_move_squares for black king'):
            ch1 = cb1.get_checker((5,2))
            self.assertTrue(ch1.color == 'black')
            ch1.king = True
            moves_list1 = ch1.get_move_squares()
            moves_list2 = ch1.get_move_squares(ch1.position)
            self.assertEqual(moves_list1, moves_list2)
            self.assertTrue(len(moves_list1) == 4)
            self.assertEqual(moves_list1, 
                ([(4, 1), (3, 0)], [(4, 3), (3, 4)], [(6, 1), (7, 0)], [(6, 3), (7, 4)]))

        with self.subTest('Testing get_move_squares for white checker'):
            ch1 = cb1.get_checker((2,3))
            self.assertTrue(ch1.color == 'white')
            moves_list1 = ch1.get_move_squares()
            moves_list2 = ch1.get_move_squares(ch1.position)
            self.assertEqual(moves_list1, moves_list2)
            self.assertTrue(len(moves_list1) == 2)
            self.assertEqual(moves_list1, ([(3, 2), (4, 1)], [(3, 4), (4, 5)]))

        with self.subTest('Testing get_move_squares for white king'):
            ch1 = cb1.get_checker((2,3))
            self.assertTrue(ch1.color == 'white')
            ch1.king = True
            moves_list1 = ch1.get_move_squares()
            moves_list2 = ch1.get_move_squares(ch1.position)
            self.assertEqual(moves_list1, moves_list2)
            self.assertTrue(len(moves_list1) == 4)
            self.assertEqual(moves_list1, 
                ([(1, 2), (0, 1)], [(1, 4), (0, 5)], [(3, 2), (4, 1)], [(3, 4), (4, 5)]))


    def test_list_moves(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        with self.subTest('Testing list_moves for black checker'):
            pass
            #self.assertEqual(cb1.get_checker((7,4)).list_moves(), [])
            #self.assertEqual(cb1.get_checker((6,3)).list_moves(), [])
            #self.assertEqual(cb1.get_checker((5,0)).list_moves(), [])

