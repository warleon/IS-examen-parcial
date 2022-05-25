from game.game import Game
from game.player import Player
from strategies.aPrime import APrime
from strategies.fiveEven import FiveEven
from strategies.fiveOdd import FiveOdd
from strategies.threeMultOfTen import ThreeMultOfTen
from strategies.twoMultOfTwentyFive import TwoMultOfTwentyFive
from threading import Thread

def player_actions(name,strat):
	game = Game()
	player = Player(name)
	game.subscribe(player,strat)


def main():
	game = Game()
	threads = [
						Thread(target = player_actions,args=('aPrime',APrime())),
						Thread(target = player_actions,args=('fiveEven',FiveEven())),
						Thread(target = player_actions,args=('fiveOdd',FiveOdd())),
						Thread(target = player_actions,args=('threeMultOfTen',ThreeMultOfTen())),
						Thread(target = player_actions,args=('twoMultOfTwentyFive',TwoMultOfTwentyFive()))
						]
	for t in threads:
		t.start()

	game.startGame()

	
		

if __name__ == "__main__":
		main()