# src/main.py

import numpy as np
import sys
from src.in_out.file_reader import read_inp_file
# from functions.gradshape_function import gradshape
from src.functions.material_property import plane_strain_tangent
from src.functions.stiffness_matrix import assemble_stiffness_matrix, apply_boundary_conditions
from src.utils.error_handling import local_error
from src.visualization.plotting import plot_displacements


def main():
	if len(sys.argv) <= 1:
		local_error("No input file provided.")
	inp_file = sys.argv[1]
	nodes, conn, boundary = read_inp_file(inp_file)
	nodes = np.array(nodes)
	C = plane_strain_tangent(E=100.0, v=0.3)
	q4 = np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]]) / np.sqrt(3)
	
	K = assemble_stiffness_matrix(nodes, conn, C, q4)
	f = np.zeros(2 * len(nodes))
	apply_boundary_conditions(K, f, boundary)
	u = np.linalg.solve(K, f)
	
	plot_displacements(nodes, u, conn)


if __name__ == "__main__":
	main()
