# Week 3 - Tutorial 3: Switches and File I/O
# Info1110 - Sandeep S
# 13/05/2018
# flags.py Program that accepts flags as command line arguments

import sys


if len(sys.argv) < 2:
	print("Need more arguments")
	sys.exit()
	

word = sys.argv[1]


i = 2
while i < len(sys.argv):
	
	if sys.argv[i][0:3] == "-f=":
		word = sys.argv[i][3:] + word
	elif sys.argv[i][0:3] == "-e=":
		word = word + sys.argv[i][3:]
	elif sys.argv[i][0:5] == "-caps":
		word = word.upper()
	
	i = i + 1
	

print("{}".format(word))

