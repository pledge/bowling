class Game:
	def __init__(self):
		self.frames = [Frame(1)]
		self.frame = 1
	
	def roll(self, pins):
		if self.frames[-1].is_complete():
			self.frame += 1
			self.frames.append(Frame(self.frame))
		
		f = self.frames[-1]
		f.roll(pins)
	
	def total(self):
		return reduce(lambda acc, f: acc + f.total(), self.frames, 0)

class Frame:
	def __init__(self, frame):
		self.frame = frame
		self.bowls = []

	def roll(self, pins):
		self.bowls.append(pins)

	def is_complete(self):
		if (self.frame != 10):
			return sum(self.bowls) == 10 or len(self.bowls) == 2
		else:
			n = len(self.bowls)
			if n == 1:
				return False
			if n == 3 :
				return True
			if n == 2 and self.bowls[0] == 10:
				return False
			if n == 2 and sum(self.bowls) == 10:
				return False
			# error here as unexpected?
			return True

	def total(self):
		return sum(self.bowls)

