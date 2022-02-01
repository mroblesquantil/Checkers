import numpy as np
from typing import List, Tuple, Union


class StateVector(np.array):
	def __init__(self):
		super(StateVector, self).__init__()

	def visualize(self) -> None:
		"""Visualize the state."""
		pass

	def _positions_of_color(self, color: bool):
		"""
		Return all the positions in which the player of color has pieces.

		Returns
		-------
			Return all the positions in which the player of color has pieces.
		"""
		pass

	def blue_positions(self) -> List[int]:
		"""
		Return all the positions in which the red player has pieces.

		Returns
		-------
			Return all the positions in which the red player has pieces.
		"""
		pass

	def red_positions(self) -> List[int]:
		"""
		Return all the positions in which the blue player has pieces.

		Returns
		-------
			Return all the positions in which the red player has pieces.
		"""


# Todo: Should we merge these two classes together??
class StateTransitions:
	def __init__(self):
		pass

	@staticmethod
	def is_valid(source_state: StateVector, target_state: StateVector) -> bool:
		"""
		Check if the transition between source_state and target_state is valid.

		Parameters
		----------
		source_state: StateVector
			Source state.
		target_state: StateVector
			Tentative next state.

		Returns
		-------
		bool:
			True if it is possible to transition from source_state into target_state given the game roules.
		"""
		pass

	@staticmethod
	def feasible_moves_piece(state: StateVector, piece_coordinate: Union[int, Tuple[int, int]]) -> List[StateVector]:
		"""
		Return the feasible moves for a piece in a given state.

		Given a StateVector and a position, it returns all the feasible moves for that piece, i.e., the feasible
		StateVector in which the given piece is moved.

		Parameters
		----------
		state: StateVector:
			The state in which the move will be made.
		piece_coordinate: Union[int, Tuple[int, int]]
			An integer or tuple representing the piece for which the next states will be computed.

		Returns
		-------
		List[StateVector]:
			List of StateVector with the feasible states resulting from moving the given piece.
		"""
		pass
