# src/in_out/file_reader.py

def read_inp_file(inp_file_name):
	"""Reads and parses the input file for nodes, elements, and boundary conditions."""
	nodes, conn, boundary = [], [], []
	state = 0
	with open(inp_file_name, 'r') as inp_file:
		for line in inp_file:
			line = line.strip()
			if len(line) <= 0 or line[0] == '*':
				state = {'*node': 1, '*element': 2, '*boundary': 3}.get(line.lower(), 0)
				continue
			if state == 1:
				values = line.split(",")
				nodes.append([float(values[1]), float(values[2])])
			elif state == 2:
				values = line.split(",")
				conn.append([int(values[i]) - 1 for i in range(1, 5)])
			elif state == 3:
				values = line.split(",")
				node_nr, dof1, dof2, val = int(values[0]) - 1, int(values[1]), int(values[2]), float(values[3])
				boundary.extend([[node_nr, dof, val] for dof in (dof1, dof2) if dof == 1 or dof == 2])
	return nodes, conn, boundary
