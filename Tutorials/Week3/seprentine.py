# Week 3 - Tutorial 3: Switches and File I/O
# Info1110 - Sandeep S
# 13/05/2018
# serpentine.py Print a snake based on character from cmd line

import sys

c = sys.argv[1]

print("{ch}        {ch}{ch}{ch}{ch}       {ch}{ch}0{ch}0{ch}".format(ch = c))
print(" {ch}      {ch}{ch} {ch}{ch}{ch}     {ch}{ch}{ch}{ch}{ch}{ch}{ch}{ch}".format(ch = c))
print("  {ch}    {ch}{ch}   {ch}{ch}{ch}   {ch}{ch}{ch}{ch}{ch}{ch} \\".format(ch = c))
print("   {ch}   {ch}{ch}    {ch}{ch}{ch} {ch}{ch}{ch}{ch}    |\\".format(ch = c))
print("    {ch}{ch}{ch}       {ch}{ch}{ch}{ch}{ch}".format(ch = c))

