# tests/test_shape_functions.py

import unittest
import numpy as np
from src.functions.shape_function import shape

class MyTestCases(unittest.TestCase):
	def test_shape_output(self):
		"""Test the output shape function values for known input."""
		xi = [1, -1]
		expected_output = np.array([0.0, 1.0, 0.0, 0.0])
		np.testing.assert_array_almost_equal(shape(xi), expected_output)
	
	def test_invalid_input(self):
		"""Test that an invalid input raises a ValueError."""
		with self.assertRaises(ValueError):
			shape([1])  # Only one element instead of two

if __name__ == "__main__":
	unittest.main()
