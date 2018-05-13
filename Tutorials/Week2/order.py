# Week 2 - Tutorial 2: Variables, Types and Formatting - INCOMPLETE
# Info1110 - Sandeep S
# 13/05/2018
# order.py 

from datetime import datetime

date = "1997-03-18"

new_date = datetime.strptime(date, "%Y-%m-%d")
print(new_date)
