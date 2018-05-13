# Week 2 - Tutorial 2: Variables, Types and Formatting
# Info1110 - Sandeep S
# 13/05/2018
# variable_assignment.py is a program that follows what variables are assigned


a = 10
b = 0

# a = 10 b = 0
print("Round 1: a = {} b = {}".format(a, b))

b = a
a += a + b

# a = 30  b = 10
print("Round 2: a = {} b = {}".format(a, b))

x = a - b
x = a * b
x -= a * b

# a= 30 b = 10 x = 0
print("Round 3: a = {} b = {} x = {}".format(a, b, x))

a = a/2

# a = 15.0 b = 10 x = 0
print("Round 4: a = {} b = {} x = {}".format(a,b,x))
