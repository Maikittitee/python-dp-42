#!/opt/homebrew/bin/python3

import sys

try:
	print(sys.argv[1])
except IndexError:
	print("none")
