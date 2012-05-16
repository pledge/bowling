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

if __name__ == '__main__':
	unittest.main()
