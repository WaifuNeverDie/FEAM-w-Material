# src/utils/error_handling.py

import sys


def local_error(message):
	print("*** ERROR ***")
	print(message)
	sys.exit(3)
