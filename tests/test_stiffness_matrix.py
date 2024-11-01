# tests/test_stiffness_matrix.py

import unittest
import numpy as np
from src.functions.stiffness_matrix import assemble_stiffness_matrix, apply_boundary_conditions
from src.functions.gradshape_function import gradshape


class MyTestCases(unittest.TestCase):
	def test_assemble_stiffness_matrix(self):
		nodes = np.array([[0.0, 0.0], [1.0, 0.0], [1.0, 1.0], [0.0, 1.0]])
		conn = [[0, 1, 2, 3]]
		C = np.identity(3)
		q4 = np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]]) / np.sqrt(3)
		
		K = assemble_stiffness_matrix(nodes, conn, C, q4)
		self.assertEqual(K.shape, (8, 8))
	
	def test_apply_boundary_conditions(self):
		K = np.identity(6)
		f = np.zeros(6)
		boundary = [[0, 1, 0.0], [1, 2, 0.1]]
		
		apply_boundary_conditions(K, f, boundary)
		self.assertEqual(f[0], 0.0)
		self.assertEqual(f[3], 0.1)
		self.assertEqual(K[0, 0], 1.0)
		self.assertTrue(np.all(K[0, 1:] == 0))


if __name__ == '__main__':
	unittest.main()
