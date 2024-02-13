#!/opt/homebrew/bin/python3

import sys

while (len(sys.argv) == 1):
	s = input("What was the parameter? ")
	if (s == sys.argv[1]):
		print("Good Job!")
	else:
		print("Nope, sorry...")
	exit()
print("none")
