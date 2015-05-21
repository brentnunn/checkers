
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

        with self.subTest('Testing list_moves'):
            self.assertEqual(cb1.get_checker((7,4)).list_moves(), [])
            self.assertEqual(cb1.get_checker((6,3)).list_moves(), [])
            self.assertEqual(cb1.get_checker((5,0)).list_moves(), [((5, 0), (4, 1))])
            self.assertEqual(cb1.get_checker((5,2)).list_moves(), 
                [((5, 2), (4, 1)), ((5, 2), (4, 3))])


    def test_move(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        with self.subTest('Testing move'):
            ch1 = cb1.get_checker((5,2))
            moves = ch1.list_moves()
            move_4_3 = moves[1]
            self.assertIsNone(cb1.get_checker((4,3)))
            ch1.move(move_4_3[1])
            self.assertIsNone(cb1.get_checker((5,2)))
            self.assertIsNotNone(cb1.get_checker((4,3)))
            ch2 = cb1.get_checker((4,3))
            self.assertEqual(ch1, ch2)


    def test_jump_methods(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        with self.subTest('Testing check_for_jump'):
            for chb1 in cb1.black_checkers:
                self.assertFalse(chb1.check_for_jump())
            for chw1 in cb1.white_checkers:
                self.assertFalse(chw1.check_for_jump())

            chb1 = cb1.get_checker((5,2))
            chb1.move((4,3))
            self.assertFalse(chb1.check_for_jump())

            chw1 = cb1.get_checker((2,1))
            chw1.move((3,2))
            self.assertFalse(chw1.check_for_jump())
            self.assertTrue(chb1.check_for_jump())

        with self.subTest('Testing list_jumps with 1 jump'):
            # Should be one jump chain in list of jumps
            self.assertEqual(len(chb1.list_jumps()), 1)
            # Jump chain should contian 2 squares
            self.assertEqual(len(chb1.list_jumps()[0]), 2)
            # Jump chain starts with checker's pre-jump position
            self.assertEqual(chb1.list_jumps()[0][0], chb1.position)
            # Jump chain ends with last square checker jumps to
            self.assertEqual(chb1.list_jumps()[0][-1], (2,1))

        with self.subTest('Testing list_jumps with 2 jump options'):
            # Setup 2nd white checker to possibly be jumped
            chw2 = cb1.get_checker((2,5))
            chw2.move((3,4))
            # Should be two jump chains in list of jumps
            self.assertEqual(len(chb1.list_jumps()), 2)
            # Both jump chains should contain 2 squares
            self.assertEqual(len(chb1.list_jumps()[0]), 2)
            self.assertEqual(len(chb1.list_jumps()[1]), 2)
            # Both jump chains start with checker's pre-jump position
            self.assertEqual(chb1.list_jumps()[0][0], chb1.position)
            self.assertEqual(chb1.list_jumps()[1][0], chb1.position)
            # Both jump chains end with last square checker jumps to
            self.assertEqual(chb1.list_jumps()[0][-1], (2,1))
            self.assertEqual(chb1.list_jumps()[1][-1], (2,5))

        with self.subTest('Testing list_jumps with a double jump option'):
            # Remove a checker to allow another checker to be jumped
            cb1.remove_checker((0,7))
            # Still only two jump chains
            self.assertEqual(len(chb1.list_jumps()), 2)
            # One jump chain still has length of 2 (jumping 1 checker)
            self.assertEqual(len(chb1.list_jumps()[0]), 2)
            # One jump chain should now have a length of 3: 
            #   Starting square, 1st jump square, 2nd jump square
            self.assertEqual(len(chb1.list_jumps()[1]), 3)
            self.assertEqual(chb1.list_jumps()[1][-1], (0,7))

        with self.subTest('Testing jump of one checker'):
            # Get jump chain to jump one checker
            num_white_checkers_pre_jump = len(cb1.white_checkers)
            jump_chain_list = chb1.list_jumps()
            chain1 = jump_chain_list[0]
            chb1.jump_chain(chain1)
            # Checker's new position should be the last square in the chain
            self.assertEqual(chb1.position, chain1[-1])
            # There should be one fewer white checkers
            self.assertEqual(num_white_checkers_pre_jump, len(cb1.white_checkers) + 1)

        with self.subTest('Testing jump of two checkers'):
            # Prepare board for jump of multiple checkers at squares (3,4) & (1,6)
            chb2 = cb1.get_checker((5,4))
            chb2.move((4,3))
            num_white_checkers_pre_jump = len(cb1.white_checkers)
            jump_chain_list = chb2.list_jumps()
            chain1 = jump_chain_list[0]
            chb2.jump_chain(chain1)
            # Checker's new position should be the last square in the chain
            self.assertEqual(chb2.position, chain1[-1])
            # There should be two fewer white checkers
            self.assertEqual(num_white_checkers_pre_jump, len(cb1.white_checkers) + 2)


    def test_checker_promotion(self):
        """ Verify non-king checkers are promoted on reaching opponent's home row """
        pass
