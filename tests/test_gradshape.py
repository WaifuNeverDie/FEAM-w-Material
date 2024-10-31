import unittest
import numpy as np
from src.functions.gradshape_function import gradshape

class MyTestCases(unittest.TestCase):
	
	def test_gradient_calculation(self):
		"""Test that gradshape calculates the correct gradient matrix."""
		xi = [0.5, -0.5]
		expected_output = np.array([
				[-0.375, 0.375, 0.125, -0.125],
				[-0.125, -0.375,  0.375, 0.125]
				])
		np.testing.assert_array_almost_equal(gradshape(xi), expected_output, decimal=4)
	
	def test_invalid_input_length(self):
		"""Test that gradshape raises a ValueError for incorrect input length."""
		with self.assertRaises(ValueError):
			gradshape([0.5])  # Only one element instead of two
	
	def test_no_rounding(self):
		"""Test that gradshape returns unrounded output when round_output is None."""
		xi = [0.3, -0.7]
		result = gradshape(xi, 3)
		# Manually calculated expected result without rounding
		expected_output = np.array([
				[-0.425,  0.425,  0.075, -0.075],
				[-0.175, -0.325, 0.325, 0.175]
				])
		np.testing.assert_array_almost_equal(result, expected_output)

if __name__ == "__main__":
	unittest.main()
