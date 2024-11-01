# src/visualization/plot_results.py

import matplotlib.pyplot as plt
import numpy as np


def plot_displacements(nodes, u, conn, result_type="e11"):
	xvec, yvec, res, tri = [], [], [], []
	for ni, pt in enumerate(nodes):
		xvec.append(pt[0] + u[2 * ni])
		yvec.append(pt[1] + u[2 * ni + 1])
		res.append(u[2 * ni] if result_type == "u1" else u[2 * ni + 1])
	for c in conn:
		tri.append([c[0], c[1], c[2]])
		tri.append([c[0], c[2], c[3]])
	t = plt.tricontourf(xvec, yvec, res, triangles=tri, levels=14, cmap=plt.cm.jet)
	plt.colorbar(t)
	plt.axis("equal")
	plt.show()
