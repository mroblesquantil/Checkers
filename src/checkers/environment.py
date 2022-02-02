import numpy as np
from typing import List, Tuple, Union

from gui import Visualizer


class StateVector(np.ndarray):

    def __new__(cls, size_of_the_board: int = 8, **kwargs):
        """
        The constructor of the class
        """

        # The size of the vector.
        n = size_of_the_board ** 2 // 2 + 1

        kwargs['shape'] = (n,)
        kwargs['dtype'] = np.int8

        obj = super().__new__(cls, **kwargs)

        obj.__init__(size_of_the_board)
        return obj

    # noinspection PyMissingConstructor
    def __init__(self, size_of_the_board: int):
        self.size_of_the_board = size_of_the_board

        pieces_per_row = self.size_of_the_board // 2
        # Todo: redefine convention. Its computationally cheaper to store ints than floats.
        #  Therefore I suggest using the convention {-2, -1, 0, 1, 2}.

        # set the value for the light pieces
        self[0: pieces_per_row * 3] = -1
        self[pieces_per_row * 3: -pieces_per_row * 3 - 1] = 0
        self[-(pieces_per_row * 3 + 1):-1] = 1

        self.turn = 0

    @property
    def turn(self):
        return self[-1]

    @turn.setter
    def turn(self, value):
        self[-1] = value

    def visualize(self) -> None:
        """Visualize the state."""
        Visualizer.filled_board(self)

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

    def from_index_to_coordinate(self, index_: int) -> Tuple[int, int]:
        """
        Maps the index of the array into a coordinate representing it's location on the board.

        Parameters
        ----------
        index_: int
            index to be mapped.

        Returns
        -------
        Tuple[int, int]:
            Coordinate representing the index location on the board.

        """
        if index_ > len(self) - 1:
            raise Exception('The given index does not lies within the board. '
                            f'The index must be less than {len(self) - 1}')
        k = index_ * 2
        n = self.size_of_the_board

        i = k // n
        j = n - k % n - 1 if i % 2 == 0 else k % n
        return i, j


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
