import unittest
from bowling import *

class GameTest(unittest.TestCase):
	
	def test_correct_start_state(self):
		g = Game()
		
		self.assertEqual(g.frame, 1)
		self.assertEqual(g.total(), 0)

	def test_running_total_no_bonus(self):
		g = Game()
		g.roll(3)
		self.assertEqual(g.running_total(), [3])
		g.roll(4)
		self.assertEqual(g.running_total(), [7])

	def test_running_total_strike(self):
		g = Game()
		g.roll(10)
		self.assertEqual(g.running_total(), [10])
		g.roll(4)
		g.roll(3)
		self.assertEqual(g.running_total(), [17, 24])
	
	def test_running_total_spare(self):
		g = Game()
		g.roll(4)
		g.roll(6)
		self.assertEqual(g.running_total(), [10])
		g.roll(4)
		g.roll(2)
		self.assertEqual(g.running_total(), [14, 20])
	
	def test_perfect_game(self):
		g = Game()
		for x in range(12):
			g.roll(10)
		self.assertEqual(g.total(), 300)
	
	def test_worst_game(self):
		g = Game()
		for x in range(20):
			g.roll(0)
		self.assertEqual(g.total(), 0)

class FrameTest(unittest.TestCase):

	def test_correct_start_state(self):
		f = Frame()
		self.assertEqual(f.bowls, [])


if __name__ == '__main__':
	unittest.main()
