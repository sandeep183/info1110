# Week 2 - Tutorial 2: Variables, Types and Formatting
# Info1110 - Sandeep S
# 13/05/2018
# boolean_exp.py is a program which looks at boolean expressions: True/False

a = True
b = False
x = 50


# Should print False
result = a and b
print("a and b = {}".format(result))

# Should print True
result = not(not(a)) or b
print("not(not(a)) ot b = {}".format(result))

# Should print True
result = a and not b or not a
print("a and not b or not a = {}".format(result))

# Should print True
result = (b and not(b)) or (a or not(a))
print("(b and not(b)) or (a or not(a)) = {}".format(result))


