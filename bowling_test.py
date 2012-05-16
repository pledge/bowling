import unittest
from bowling import *

class GameTest(unittest.TestCase):
	
	def test_correct_start_state(self):
		g = Game()
		
		self.assertEqual(g.frame, 1)
		self.assertEqual(g.total(), 0)
	
	def test_perfect_game(self):
		g = Game()
		for x in range(12):
			g.roll(10)
		self.assertEqual(g.total(), 300)

class FrameTest(unittest.TestCase):

	def test_correct_start_state(self):
		f = Frame(1)
		self.assertEqual(f.bowls, [])


if __name__ == '__main__':
	unittest.main()
