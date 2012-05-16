import unittest
from bowling import *

class GameTest(unittest.TestCase):
	
	def test_correct_start_state(self):
		g = Game()
		
		self.assertEqual(g.frames, [])
		self.assertEqual(g.frame, 1)

class FrameTest(unittest.TestCase):

	def test_correct_start_state(self):
		f = Frame()
		self.assertEqual(f.bowls, [])

	def test_is_strike(self):
		f = Frame()
		f.roll(10)
		self.assertTrue(f.isStrike())

		f2 = Frame()
		f2.roll(1)
		self.assertFalse(f2.isStrike())
		f2.roll(2)
		self.assertFalse(f2.isStrike())

		f3 = Frame()
		f2.roll(5)
		f2.roll(5)
		self.assertFalse(f3.isStrike())
	
	def test_is_spare(self):
		f = Frame()
		f.roll(5)
		f.roll(5)
		self.assertTrue(f.isSpare())

		f2 = Frame()
		f2.roll(5)
		f2.roll(4)
		self.assertFalse(f2.isSpare())


if __name__ == '__main__':
	unittest.main()
