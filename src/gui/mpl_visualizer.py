from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from matplotlib.animation import FuncAnimation

import numpy as np
import os
from typing import List

from checkers.piece import PieceHelper


class Visualizer:
	piece_images = {PieceHelper.dark * PieceHelper.queen: os.path.realpath('data/gui_data/black_queen.png'),
	                PieceHelper.dark * PieceHelper.piece: os.path.realpath('data/gui_data/black_piece.png'),
	                PieceHelper.light * PieceHelper.queen: os.path.realpath('data/gui_data/white_queen.png'),
	                PieceHelper.light * PieceHelper.piece: os.path.realpath('data/gui_data/white_piece.png')}

	@staticmethod
	def show():
		plt.show()

	@staticmethod
	def plain_board(dimension=8):
		n = dimension
		image = np.array([[1 if (i + j) % 2 == 0 else 0 for j in range(n)] for i in range(n)], dtype=float)
		return image

	@staticmethod
	def board(dimension=8):
		n = dimension
		board = Visualizer.plain_board(n)
		fig, ax = plt.subplots()
		row_labels = list(range(1, n + 1))
		col_labels = list(range(1, n + 1))
		ax.matshow(board, cmap='gist_ncar')
		plt.xticks(range(n), col_labels)
		plt.yticks(range(n), row_labels)

		return fig, ax

	@staticmethod
	def plot_piece(ax, i, j, piece: int):
		arr_lena = mpimg.imread(Visualizer.piece_images[piece])

		imagebox = OffsetImage(arr_lena, zoom=0.3)
		ab = AnnotationBbox(imagebox, (j, i), frameon=False)
		ax.add_artist(ab)
		plt.draw()

	@staticmethod
	def visualize_state(board: 'StateVector'):
		fig, ax = Visualizer.board(board.size_of_the_board)

		for k in range(len(board) - 1):
			piece = board[k]
			if piece != PieceHelper.empty_square:
				i, j = board.from_index_to_coordinate(k)
				Visualizer.plot_piece(ax, i, j, board[k])

		return fig, ax

	@staticmethod
	def visualize_game(states: List['StateVector']):
		# Todo: check and improve this method.
		fig, ax = plt.subplots()

		ani = FuncAnimation(fig, update=Visualizer.visualize_state, frames=states, blit=True)
		return ani

