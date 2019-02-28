from game import Game
import unittest


class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()


if __name__ == '__main__':
    unittest.main()