from game.singleton import SingletonMeta
from threading import Lock
from random import randint


class Game(metaclass=SingletonMeta):
	def __init__(self):
		self.players = []
		self.subLock = Lock()

	def subscribe(self, player,strategy):
		with self.subLock:
			self.players.append((player,strategy))
		self.notify(f'{player.name} has joined the game')

	def notify(self, message):
		for player,strategy in self.players:
			player.notify(message)

	def check_win(self,number):
		for player,strategy in self.players:
			if strategy.check_win(number):
				self.notify(f'{player.name} won!')
				return True
		return False

	def generate_number(self):
		value = randint(0, 100)
		self.notify(f'The number is {value}')
		return value

	def startGame(self):
		while(1):
			if self.check_win(self.generate_number()):
				return
