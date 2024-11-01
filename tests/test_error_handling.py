# tests/test_error_handling.py

import unittest
from src.utils.error_handling import local_error


class MyTestCases(unittest.TestCase):
	def test_local_error(self):
		with self.assertRaises(SystemExit) as cm:
			local_error("Test error")
		self.assertEqual(cm.exception.code, 3)


if __name__ == '__main__':
	unittest.main()
