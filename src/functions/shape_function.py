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


# src/functions/gradshape_function.py


import numpy as np
from typing import List, Union


def gradshape(xi_vals: List[Union[float, int]], round_output: int = 4) -> np.ndarray:
	"""
	Calculates the gradient of the shape functions for a 4-node, isoparametric element.

	This function returns the partial derivatives of each shape function (dN) with respect to
	the local coordinates xi and eta, which are typically used in finite element analysis.

	Parameters:
		xi (List[float, int]): A 1x2 list containing the local coordinates [xi, eta].
		round_output (int, optional): Number of decimal places to round the output.
		                              Default is 4. Set to None to avoid rounding.

	Returns:
		np.ndarray: A 2x4 array representing the gradients of the shape functions with
		            respect to xi and eta:
		            [[dN1/dxi, dN2/dxi, dN3/dxi, dN4/dxi],
		             [dN1/deta, dN2/deta, dN3/deta, dN4/deta]]

	Raises:
		ValueError: If the input list `xi` does not contain exactly two elements.
	"""
	if len(xi_vals) != 2:
		raise ValueError("Input xi must be a 1x2 list [xi, eta].")
	
	# Unpack xi and eta from the input list
	xi, eta = xi_vals
	
	# Gradient matrix calculation
	dN = [
			[-(1.0 - eta), (1.0 - eta), (1.0 + eta), -(1.0 + eta)],
			[-(1.0 - xi), -(1.0 + xi), (1.0 + xi), (1.0 - xi)]
			]
	
	# Convert to numpy array and scale by 0.25
	gradient = 0.25 * np.array(dN)
	
	# Round output if specified
	if round_output is not None:
		gradient = np.round(gradient, round_output)
	
	return gradient
