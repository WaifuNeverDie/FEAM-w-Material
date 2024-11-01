import unittest
import numpy as np
from src.functions.material_property import plane_strain_tangent


class TestPlaneStrainTangent(unittest.TestCase):
	
	def test_plane_strain_tangent_basic(self):
		"""Test calculation of plane strain tangent matrix for a basic case."""
		E = 100.0
		v = 0.3
		expected_output = np.array(
				[
						[109.8901, 32.9670, 0.0],
						[32.9670, 109.8901, 0.0],
						[0.0, 0.0, 32.9670]
						]
				)
		result = plane_strain_tangent(E, v)
		np.testing.assert_array_almost_equal(result, expected_output, decimal=4)
	
	def test_invalid_poissons_ratio(self):
		"""Test that the function raises ValueError for invalid Poisson's ratio."""
		E = 100.0
		invalid_v_values = [-1.5, 0.6]  # Values outside the valid range
		for v in invalid_v_values:
			with self.assertRaises(ValueError):
				plane_strain_tangent(E, v)
	
	def test_varied_material_properties(self):
		"""Test the function with a variety of valid E and v values."""
		test_cases = [
				(200.0, 0.25, np.array([[160.0, 53.3333, 0.0], [53.3333, 160.0, 0.0], [0.0, 0.0, 53.3333]])),
				(150.0, 0.2, np.array([[150.0, 37.5, 0.0], [37.5, 150.0, 0.0], [0.0, 0.0, 56.25]])),
				(300.0, 0.35, np.array([[250.0, 83.3333, 0.0], [83.3333, 250.0, 0.0], [0.0, 0.0, 50.0]]))
				]
		
		for E, v, expected_output in test_cases:
			result = plane_strain_tangent(E, v)
			np.testing.assert_array_almost_equal(result, expected_output, decimal=4)


if __name__ == "__main__":
	unittest.main()
