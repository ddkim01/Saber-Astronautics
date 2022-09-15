#
# Author: David Kim (z5255322@ad.unsw.edu.au)
#
# Date: September 2022
#
# Task: Saber Astronautics Technical Test 1
#
# Function: Create and print list with conditions
#
# Description: This script should print numbers from 1 to 75 where:
#               - Multiples of 4 print "Mission"
#               - Multiples of 5 print "Control"
#               - Multiples of 4 & 7 print "Mission"
#
# Parameters: using print(), for loop, and conditional statements.
#
# Return: printed list of numbers and strings.
#
# Bugs: Note that script is altered to ignore multiples of 4 & 7 and checks for 4 & 5 instead
#       otherwise multiples of 4 & 5 print "Mission" and never print "Control".
#       Multiples of 7 diminishes the relevance of checking for multiples of 5
#
# Sources: none
#
# Status: Finished.
#
# =======================================================================================
#

# Range(a, b) initialises from a to b non-inclusive hence b = 76 and not 75.
for i in range(1, 76):
    # Note that order of the conditional statements matters.
    # This statement is first to cover mutually inclusive events first.
    if i % 4 == 0 and i % 5 == 0:
        print("Mission Control")
    elif i % 4 == 0:
        print("Mission")
    elif i % 5 == 0:
        print("Control")
    else:
        print(i)
