
import unittest
import checkerboard as cb
import checker as ch


class testCheckerboard(unittest.TestCase):
    """ Tests for the Checkerboard class """

    def test_init(self):
        cb1 = cb.Checkerboard()

        # Verify 8 rows in checkerboard
        self.assertEqual(len(cb1.squares), 8)

        # Verify each row has 8 columns
        for row in cb1.squares:
            self.assertEqual(len(row), 8)


    def test_setup_new_board(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        # Verify each color has 12 checkers
        with self.subTest('Testing number of distinct checkers'):
            self.assertEqual(len(set(cb1.black_checkers)), 12)
            self.assertEqual(len(set(cb1.white_checkers)), 12)

        # Verify checkers' positions
        with self.subTest('Testing checker positions'):
            for checker in cb1.black_checkers:
                row, column = checker.position
                self.assertEqual(checker, cb1.squares[row][column])
                self.assertTrue(row > 4)
                self.assertTrue((row + column) % 2 != 0)

            for checker in cb1.white_checkers:
                row, column = checker.position
                self.assertEqual(checker, cb1.squares[row][column])
                self.assertTrue(row < 3)
                self.assertTrue((row + column) % 2 != 0)

        # Verify checkerboard hosts 24 checkers in all squares
        pass


    def test_get_checker(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        with self.subTest('Testing get checker'):
            self.assertTrue(cb1.squares[7][6])
            ch1 = cb1.squares[7][6]
            ch2 = cb1.get_checker((7, 6))
            self.assertTrue(ch1 == ch2)
            self.assertTrue(ch2.position == (7,6))


    def test_remove_checker(self):
        cb1 = cb.Checkerboard()
        cb1.setup_new_board()

        with self.subTest('Testing removing checker'):
            self.assertTrue(cb1.squares[5][2])
            self.assertEqual(len(set(cb1.black_checkers)), 12)
            cb1.remove_checker((5, 2))
            self.assertEqual(len(set(cb1.black_checkers)), 11)
            self.assertFalse(cb1.squares[5][2])


    def test_place_checker(self):
        cb1 = cb.Checkerboard()

        ch1 = ch.Checker('black', cb1)
        cb1.place_checker((5, 0), ch1)

        with self.subTest('Testing place checker'):
            self.assertTrue(cb1.squares[5][0])
            self.assertEqual(ch1, cb1.squares[5][0])
            self.assertTrue(ch1.position == (5, 0))
            self.assertTrue(ch1.checkerboard == cb1)


if __name__ == '__main__':
    unittest.main()
