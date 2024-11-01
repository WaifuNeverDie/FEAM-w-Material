# src/functions/shape_functions.py

import numpy as np


def shape(xi):
	xi, eta = tuple(xi)
	N = [(1.0 - xi) * (1.0 - eta), (1.0 + xi) * (1.0 - eta),
	     (1.0 + xi) * (1.0 + eta), (1.0 - xi) * (1.0 + eta)]
	return 0.25 * np.array(N)


def gradshape(xi):
	xi, eta = tuple(xi)
	dN = [[-(1.0 - eta), (1.0 - eta), (1.0 + eta), -(1.0 + eta)],
	      [-(1.0 - xi), -(1.0 + xi), (1.0 + xi), (1.0 - xi)]]
	return 0.25 * np.array(dN)
