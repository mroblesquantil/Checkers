from abc import ABC, abstractmethod
from checkers.environment import StateVector, StateTransitions


class CheckersPlayer(ABC):
	"""
	Abstract class that represents a checkers player.

	Every instance needs to implement the `next_move` method that defines its policy.
	"""
	def __init__(self):
		pass

	@abstractmethod
	def next_move(self, state: StateVector) -> StateVector:
		"""
		Abstract method that will define each player's strategy.

		Parameters
		----------
		state: StateVector
			The state in which the player needs to take the move.

		Returns
		-------
		StateVector:
			The state in which the game will be after the move of the player.
		"""
		...


class UniformPlayer(CheckersPlayer):
	"""Represents a player whose strategy is to choose randomly among the feasible moves."""
	def next_move(self, state: StateVector) -> StateVector:
		"""
		Chooses a random uniform move given the state.

		Parameters
		----------
		state: StateVector
			The state in which the player needs to take the move.

		Returns
		-------
		StateVector:
			The state in which the game will be after the move of the player.
		"""
		pass
