import unittest

from game import Game


class TestBowlingGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()
    

if __name__ == "__main__":
    unittest.main()