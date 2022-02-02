from matplotlib.offsetbox import TextArea, DrawingArea, OffsetImage, AnnotationBbox
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import os


class Visualizer:
	piece_images = {-2: os.path.realpath('data/gui_data/black_queen.png'),
	                -1: os.path.realpath('data/gui_data/black_piece.png'),
	                2: os.path.realpath('data/gui_data/white_queen.png'),
	                1: os.path.realpath('data/gui_data/white_piece.png')}

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
		row_labels = list(range(1, n + 1))[:: -1]
		col_labels = list(range(1, n + 1))
		ax.matshow(board, cmap='gist_ncar')
		plt.xticks(range(n), col_labels)
		plt.yticks(range(n), row_labels)

		return fig, ax

	@staticmethod
	def plot_piece(ax, i, j, piece: int):
		arr_lena = mpimg.imread(Visualizer.piece_images[piece])

		imagebox = OffsetImage(arr_lena, zoom=0.2)
		ab = AnnotationBbox(imagebox, (j, i), frameon=False)
		ax.add_artist(ab)
		plt.draw()

	@staticmethod
	def filled_board(board: 'StateVector'):
		fig, ax = Visualizer.board(board.size_of_the_board)

		for k in range(len(board) - 1):
			piece = board[k]
			if piece != 0:
				i, j = board.from_index_to_coordinate(k)
				Visualizer.plot_piece(ax, i, j, board[k])

		return fig, ax
