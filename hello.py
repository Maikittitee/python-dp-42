import re

string = "abbc"

reg = "ab{1,2}c"

if (re.match(reg, string)):
	print("ok")
else:
	print("ko")