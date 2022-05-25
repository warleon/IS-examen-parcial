
class Player():
	def __init__(self, name):
		self.name = name
	
	def notify(self, message):
		print(f'{self.name} got notified: {message}')