# tests/test_file_reader.py

import unittest
from src.in_out.file_reader import read_inp_file


class MyTestCases(unittest.TestCase):
	def test_read_inp_file(self):
		nodes, conn, boundary = read_inp_file('sample_input.inp')
		self.assertEqual(len(nodes), 4)
		self.assertEqual(len(conn), 1)
		self.assertEqual(len(boundary), 5)
		self.assertEqual(nodes[0], [0.0, 0.0])
		self.assertEqual(conn[0], [0, 1, 2, 3])
		self.assertEqual(boundary[0], [0, 1, 0.0])


if __name__ == '__main__':
	unittest.main()
