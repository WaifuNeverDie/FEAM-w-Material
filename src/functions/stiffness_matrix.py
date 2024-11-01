# src/functions/stiffness_matrix.py

import numpy as np
from shape_function import gradshape

def assemble_stiffness_matrix(nodes, conn, C, q4):
	num_nodes = len(nodes)
	K = np.zeros((2 * num_nodes, 2 * num_nodes))
	B = np.zeros((3, 8))
	
	for c in conn:
		node_pts = nodes[c, :]
		Ke = np.zeros((8, 8))
		for q in q4:
			dN = gradshape(q)
			J = np.dot(dN, node_pts).T
			dN = np.dot(np.linalg.inv(J), dN)
			B[0, 0::2], B[1, 1::2], B[2, 0::2], B[2, 1::2] = dN[0], dN[1], dN[1], dN[0]
			Ke += np.dot(np.dot(B.T, C), B) * np.linalg.det(J)
		for i, I in enumerate(c):
			for j, J in enumerate(c):
				K[2 * I:2 * I + 2, 2 * J:2 * J + 2] += Ke[2 * i:2 * i + 2, 2 * j:2 * j + 2]
	return K


def apply_boundary_conditions(K, f, boundary):
	for node, dof, val in boundary:
		j = 2 * node + (dof - 1)
		K[j, :] = 0.0
		K[j, j] = 1.0
		f[j] = val
