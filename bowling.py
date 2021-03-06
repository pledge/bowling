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
		return f.is_complete()

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

class Player():
	def __init__(self, name):
		self.name = name
		self.game = Game()

	def turn(self, pins):
		return self.game.roll(pins)

class Bowling():

	def __init__(self):
		self.players = []

	def play(self):
		self.title()
		print "Enter player names.  Blank to finish"
		self._enter_players()

		for frame in range(1,11):
			self.dsep()
			print 'Frame ', frame
			self.sep()
			for player in self.players:
				while not self._turn(player):
					pass
			self._scoreboard()

		winner = max(self.players, key = lambda p : p.game.total())
		print "The winner is", winner.name

	def _turn(self, player):
		while True:
			print 'Turn for', player.name
			try:
				pins = int(raw_input('Pins: '))
				if not pins in range(0,11):
					raise ValueError
				break
			except ValueError:
				print "Number of pins must be between 0 and 10"

		return player.turn(pins)

	def _enter_players(self):
		while True:
			name = raw_input('Enter name: ')
			if name == '':
				break
			if(any(name == player.name for player in self.players)):
				print 'Name already taken already. Please enter another.'
			else:
				self.players.append(Player(name))
		if not self.players:
			print 'Zero players.  No game to be played :('
			exit()
	
	def _scoreboard(self):
		for player in self.players:
			game = player.game
			self.sep()
			print player.name
			print 'Frames',
			for i, val in enumerate(game.frames):
				print val.bowls,
			print '\n Total', game.running_total()
		print "Team total is", reduce(lambda acc, player: acc + player.game.total(), self.players, 0)

	def dsep(self):
		print "=" * 100
	def sep(self):
		print "-" * 100
	def title(self):
		message = """
 mmmmm                ""#      "                 
 #    #  mmm  m     m   #    mmm    m mm    mmmm 
 #mmmm" #" "# "m m m"   #      #    #"  #  #" "# 
 #    # #   #  #m#m#    #      #    #   #  #   # 
 #mmmm" "#m#"   # #     "mm  mm#mm  #   #  "#m"# 
                                            m  # 
                                             ""  
"""
		print message
if __name__ == '__main__':
	b = Bowling()
	b.play()
