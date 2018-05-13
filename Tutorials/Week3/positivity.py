# Week 3 - Tutorial 3: Switches and File I/O
# Info1110 - Sandeep S
# 13/05/2018
# positivity.py Using the command line argument to vary code

import sys


if len(sys.argv) == 2:
	num = int(sys.argv[1])
	num = num * 2
	print("The number is: {}".format(num))
elif len(sys.argv) == 3:
	num1 = int(sys.argv[1])
	num2 = int(sys.argv[2])
	
	if num1 > num2:
		print("{} is larger".format(num1))
	elif num2 > num1:
		print("{} is larger".format(num2))
	else:
		print("Numbers are equal")

else:
	print("The problem is too hard!")


