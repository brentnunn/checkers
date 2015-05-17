
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
        with self.subTest('Testing cecker positions'):
            pass


if __name__ == '__main__':
    unittest.main()
