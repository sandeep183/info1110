# Week 1 - Tutorial 1: Introduction, Terminal and Output
# Info1110 - Sandeep S
# 11/05/2018
# sum_numbers.py: A program that takes 3 numbers from std input and then
# displays the sum of these numbers

print("Hello")
print("I will add three numbers for you")
print("Enter three whole numbers on one line")

line = input()
n1, n2, n3 = line.split(" ")

n1 = int(n1)
n2 = int(n2)
n3 = int(n3)

total = n1 + n2 + n3

print("The sum of your numbers is: {}".format(total)) 
