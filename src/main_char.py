# src/main_char.py

import numpy as np
import sys
# from in_out.file_reader import read_inp_file
# from functions.gradshape_function import gradshape
# from functions.material_property import plane_strain_tangent
# from functions.stiffness_matrix import assemble_stiffness_matrix, apply_boundary_conditions
# from utils.error_handling import local_error
# from visualization.plotting import plot_displacements
import in_out.file_reader as rw
import functions.material_property as mp
import functions.stiffness_matrix as st
import utils.error_handling as eh
import visualization.plotting as pt


def main():
	if len(sys.argv) <= 1:
		eh.local_error("No input file provided.")
	inp_file = sys.argv[1]
	nodes, conn, boundary = rw.read_inp_file(inp_file)
	nodes = np.array(nodes)
	C = mp.plane_strain_tangent(E=100.0, v=0.3)
	q4 = np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]]) / np.sqrt(3)
	
	K = st.assemble_stiffness_matrix(nodes, conn, C, q4)
	f = np.zeros(2 * len(nodes))
	st.apply_boundary_conditions(K, f, boundary)
	u = np.linalg.solve(K, f)
	
	pt.plot_displacements(nodes, u, conn)


if __name__ == "__main__":
	main()
