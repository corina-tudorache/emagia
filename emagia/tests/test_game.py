import unittest
from code.game import Battle


class GameTest(unittest.TestCase):
	def setUp(self):
		self.battle = Battle()

	def test_play(self):
		self.battle.play()


if __name__ == '__main__' and __package__ is None:
    unittest.main()
