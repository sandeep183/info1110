# Week 2 - Tutorial 2: Variables, Types and Formatting
# Info1110 - Sandeep S
# 13/05/2018
# state_execution.py Carfully monitor the types of the variables as they are
# changed

a = 3
b = 4
a = '3'

# a = str, b = int
print("Type of a = {}, Type of b = {}".format(type(a), type(b)))

print(a)
j = a + str(b)
print('The value of j is: ' + j)
b += 0.5

# j = str, b = float
print("Type of j = {}, Type of b = {}".format(type(j), type(b)))

o = j
o = len(j) < 2
t = str(o) + j

# o = bool, t = str
print("Type of o = {}, Type of t = {}".format(type(o), type(t)))
