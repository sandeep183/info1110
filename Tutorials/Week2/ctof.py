# Week 2 - Tutorial 2: Variables, Types and Formatting
# Info1110 - Sandeep S
# 13/05/2018
# ctof.py Conversion of Celsius to Fahrenheit

celsius = input("Degrees in celsius: ")
celsius = float(celsius)

fahrenheit = celsius * 9/5 + 32

print("Conversion to fahrenheit is: {:.2f}".format(fahrenheit))
