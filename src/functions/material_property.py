import numpy as np
# from typing import Union

# src/functions/material_properties.py



def plane_strain_tangent(E, v):
	"""Calculates the material tangent matrix for plane strain."""
	coef = E / ((1.0 + v) * (1.0 - 2.0 * v))
	return coef * np.array(
			[[1.0 - v, v, 0.0],
			 [v, 1.0 - v, 0.0],
			 [0.0, 0.0, 0.5 - v]]
			)


# def plane_strain_tangent(E: Union[float, int], v: Union[float, int]) -> np.ndarray:
# 	"""
# 	Calculates the material tangent matrix `C` for a plane-strain condition.
#
# 	Parameters:
# 		E (float or int): Modulus of elasticity of the material.
# 		v (float or int): Poisson's ratio of the material.
#
# 	Returns:
# 		np.ndarray: A 3x3 plane-strain material tangent matrix `C`.
#
# 	Formula:
# 		C = (E / ((1 + v) * (1 - 2 * v))) * [
# 		      [1 - v, v, 0],
# 		      [v, 1 - v, 0],
# 		      [0, 0, 0.5 - v]
# 		    ]
#
# 	Example:
# 		>>> C = plane_strain_tangent(100.0, 0.3)
# 		>>> print(C)
# 		[[109.89010989  32.96703297   0.        ]
# 		 [ 32.96703297 109.89010989   0.        ]
# 		 [  0.           0.          32.96703297]]
#
# 	Raises:
# 		ValueError: If the Poisson's ratio is outside the valid range (-1 < v < 0.5).
# 	"""
# 	# Check for valid Poisson's ratio range
# 	if not (-1.0 < v < 0.5):
# 		raise ValueError("Poisson's ratio `v` must be between -1 and 0.5 for a valid material.")
#
# 	# Calculate the coefficient
# 	coef = E / ((1.0 + v) * (1.0 - 2.0 * v))
#
# 	# Define the plane-strain tangent matrix
# 	C = coef * np.array(
# 			[
# 					[1.0 - v, v, 0.0],
# 					[v, 1.0 - v, 0.0],
# 					[0.0, 0.0, 0.5 - v]
# 					]
# 			)
#
# 	return C
