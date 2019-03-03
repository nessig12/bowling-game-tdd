from game import Game
import unittest

class TestBowlingGame(unittest.TestCase):
    def setUp(self):
        self.game = Game()

    def rollMany(self,n, pins):
        for i in range(n):
            Game.roll(self.game, pins)

    def testGutterBall(self):
        self.rollMany(20, 0)
        self.assertEqual(0, Game.score(self.game))

    def testAllOnes(self):
        self.rollMany(20, 1)
        self.assertEqual(20, Game.score(self.game))

    def testOneSpare(self):
        self.rollSpare()
        Game.roll(self.game, 3)
        self.rollMany(17, 0)
        self.assertEqual(16, Game.score(self.game))

    def testOneStrike(self):
        self.rollStrike()
        Game.roll(self.game, 3)
        Game.roll(self.game, 4)
        self.rollMany(16, 0)
        self.assertEqual(24, Game.score(self.game))

    def testPerfectGame(self):
        self.rollMany(12, 10)
        self.assertEqual(300, Game.score(self.game))

    def rollSpare(self):
        Game.roll(self.game, 5)
        Game.roll(self.game, 5)

    def rollStrike(self):
        Game.roll(self.game, 10)

if __name__ == '__main__':
    unittest.main()
