# Week 2 - Tutorial 2: Variables, Types and Formatting
# Info1110 - Sandeep S
# 13/05/2018
# ftoc.py Conversion from fahrenheit to celsius

fahrenheit = input("Temperature in Fahrenheit: ")
fahrenheit = float(fahrenheit)

celsius = (fahrenheit - 32) * 5/9

print("Degrees in celsius: {:.2f}".format(celsius))
