from checkers import StateVector, StateTransitions, CheckersGame, UniformPlayer

import numpy as np
import matplotlib.pyplot as plt


def simulate_visual(portion=None):
	game = CheckersGame(
		light_player=UniformPlayer(),
		dark_player=UniformPlayer()
	)

	history, winner = game.simulate_game()

	print(f'the winner is {winner}')
	if portion is None:
		for s in history:
			s.visualize()

	else:
		for s in history[-portion:]:
			s.visualize()


def simulate():
	game = CheckersGame(
		light_player=UniformPlayer(),
		dark_player=UniformPlayer()
	)

	history, winner = game.simulate_game()
	return history, winner


if __name__ == '__main__':
	simulate_visual(2)
