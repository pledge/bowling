class Game:
	def __init__(self):
		self.frame = 1
		self.frames = [self._create_frame()]
	
	def roll(self, pins):
		if self.frames[-1].is_complete():
			self.frame += 1
			self.frames.append(self._create_frame())
		
		f = self.frames[-1]
		f.roll(pins)

	def running_total(self):
		result = []

		def flatten(acc, f):
			acc.extend(f.bowls)
			return acc

		flat = reduce(flatten, self.frames, [])
		pos =  -1

		for i, val in enumerate(self.frames):
			bonus = 0
			if val.isStrike():
				pos += 1
				bonus = sum(flat[pos+1:pos+3])
			elif val.isSpare():
				pos += 2
				bonus = sum(flat[pos+1:pos+2])
			else:
				pos += len(val.bowls)

			prev = result[i - 1] if result else 0
			result.append(prev + val.total() + bonus)
		return result
	
	def total(self):
		return self.running_total()[-1]
	
	def _create_frame(self):
		if(self.frame == 10):
			return Frame10()
		return Frame()

class Frame:
	def __init__(self,):
		self.bowls = []

	def roll(self, pins):
		self.bowls.append(pins)

	def is_complete(self):
		return sum(self.bowls) == 10 or len(self.bowls) == 2

	def total(self):
		return sum(self.bowls)
	
	def isStrike(self):
		return self.is_complete() and self.bowls[0] == 10
	
	def isSpare(self):
		return self.is_complete() and sum(self.bowls) == 10

class Frame10(Frame):
	def __init__(self):
		Frame.__init__(self)
	
	def is_complete(self):
		n = len(self.bowls)
		if n == 2 and (self.bowls[0] == 10 or sum(self.bowls) == 10):
			return False
		return n != 1

	def total(self):
		return self.bowls[0] if self.bowls else 0
