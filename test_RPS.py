from RPS import RockPaperScissors
import unittest
from unittest.mock import patch
import random

class TestRockPaperScissors(unittest.TestCase):


    def setUp(self):
        self.game = RockPaperScissors()
        self.patcher = patch('builtins.input', return_value='Rock')
        self.patcher.start()
        #print('running test')

    def tearDown(self):
        self.patcher.stop()

    def test_valid_user_input(self):
        self.assertIn(self.game.get_inputs(), ['Rock', 'Paper', 'Scissors'])

    def test_valid_computer_input(self):
        self.game.computer_random_choice()
        self.assertIn(self.game.comp_input, ['Rock', 'Paper', 'Scissors'])

    def test_compare_user_and_comp(self):
        self.game.user_input = 'Rock'
        self.game.comp_input = 'Scissors'
        self.game.compare_user_and_comp()
        self.assertEqual(self.game.user_points, 1)

if __name__ == '__main__':
    unittest.main()