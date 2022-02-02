from checkers import StateVector
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
	state = StateVector(size_of_the_board=8)
	state[0: 3] = -2
	state.visualize()
	plt.show()

	print(state)