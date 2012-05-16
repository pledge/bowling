class Game:
	def __init__(self):
		self.frames = []
		self.frame = 1
	
	def roll(self, pins):
		pass

class Frame:
	def __init__(self):
		self.bowls = []

	def roll(self, pins):
		self.bowls.append(pins)

	def isStrike(self):
		return len(self.bowls) == 1 and sum(self.bowls) == 10

	def isSpare(self):
		return len(self.bowls) == 2 and sum(self.bowls) == 10
