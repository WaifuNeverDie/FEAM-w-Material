# tests/test_plot_results.py

import unittest
import numpy as np
from src.visualization.plotting import plot_displacements


class MyTestCases(unittest.TestCase):
	def test_plot_displacements(self):
		nodes = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
		u = np.array([0.0, 0.0, 0.1, 0.0, 0.1, 0.1, 0.0, 0.1])
		conn = [[0, 1, 2, 3]]
		
		try:
			plot_displacements(nodes, u, conn, "u1")
		except Exception as e:
			self.fail(f"plot_displacements raised an exception: {e}")


if __name__ == '__main__':
	unittest.main()
