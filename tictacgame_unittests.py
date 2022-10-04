import unittest
from tictacgame import TicTacGame
from custom_exceptions import CellOcupiedError


class TestTicTacGame(unittest.TestCase):
    def setUp(self):
        self.n = 3
        self.TicTacGame = TicTacGame(self.n)

    def test_validate_input(self):
        self.assertEqual(self.TicTacGame.validate_input(3, 'X'), None)
        self.assertRaises(IndexError, self.TicTacGame.validate_input, 10, '0')
        self.assertRaises(
            ValueError, self.TicTacGame.validate_input, 'string', 'x')
        self.assertRaises(CellOcupiedError,
                          self.TicTacGame.validate_input, 3, 'O')

    def test_check_winner(self):
        case_1 = self.TicTacGame.cells = [['0', 'X', '0'], [
            '0', 'X', 'X'], ['X', '0', 'X']]  # проверка на ничью
        self.assertEqual(self.TicTacGame.check_winner(9, 'X'), None)

        case_2 = self.TicTacGame.cells = [['X', 2, '0'], [
            'X', '0', 6], ['X', 8, 9]]  # проверка на победу в столбце
        self.assertEqual(self.TicTacGame.check_winner(5, 'X'), True)

        case_3 = self.TicTacGame.cells = [['X', 'X', 3], [
            '0', '0', '0'], [7, 8, 'X']]  # проверка на победу в строке
        self.assertEqual(self.TicTacGame.check_winner(6, '0'), True)

        case_4 = self.TicTacGame.cells = [['X', '0', 3], [4, 'X', '0'],
                                          [7, 8, 'X']]  # проверка на победу в правой диагонали
        self.assertEqual(self.TicTacGame.check_winner(5, 'X'), True)

        case_5 = self.TicTacGame.cells = [['X', 'X', '0'], ['X', '0', 6],
                                          ['0', 8, 9]]  # проверка на победу в левой диагонали
        self.assertEqual(self.TicTacGame.check_winner(6, 'O'), True)

    def test_mode_comp_vs_comp(self):
        self.assertNotEqual(self.TicTacGame.mode_comp_vs_comp(), False)

    def tearDown(self):
        print('Test done')


if __name__ == '__main__':
    unittest.main()
