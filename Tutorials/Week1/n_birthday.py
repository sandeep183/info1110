# Week 1 - Tutorial 1: Introduction, Terminal and Output
# Info1110 - Sandeep S
# 11/05/2018
# n_birthday.py: Program which works out in which year a persons nth birthday 
# will occur

birthyear = input("Enter the year when you were born: ")
birthyear = int(birthyear)

desired_age = input("Enter your desired age: ")
desired_age = int(desired_age)

final_year = birthyear + desired_age

print("You will be {} in {}".format(desired_age, final_year))
