import numpy as np
import math as m
from pandas.core.window.doc import numba_notes


def global_stiffness_matrix(num_nodes: int) -> np.ndarray:

	K = np.zeros((2 * num_nodes, 2*num_nodes))
	q4 = np.array([[-1, -1], [1, -1], [-1, 1], [1, 1]]) / math.sqrt(3.0)
	
	return K
