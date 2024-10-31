# src/functions/shape_function.py

import numpy as np
from typing import List

def shape(xi_vals: List[float]) -> np.ndarray:
	"""
	Shape functions for a 4-node, isoparametric element.
	
	Parameters:
		xi (List[float]): A list [xi, eta] representing coordinates in parametric space.
		
	Returns:
		np.ndarray: A 1x4 array with shape function values.
		
	Raises:
		ValueError: If the input list `xi` does not contain exactly 2 elements.
	"""
	if len(xi_vals) != 2:
		raise ValueError("Input xi must be a 1x2 list [xi, eta].")
	
	xi, eta = xi_vals  # Unpack xi and eta
	N = [
			(1.0 - xi) * (1.0 - eta),
			(1.0 + xi) * (1.0 - eta),
			(1.0 + xi) * (1.0 + eta),
			(1.0 - xi) * (1.0 + eta)
			]
	
	return np.round(0.25 * np.array(N), 4)
