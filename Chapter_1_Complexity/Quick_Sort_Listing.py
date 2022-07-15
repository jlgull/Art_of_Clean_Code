#! / bin / python3
#
# Author: Jonathan Heard
# Work from 'Art of Clean Code'
#
# Program name: Bubble_Sort_Listing.py
#

""" Import all the needed external methods """
import matplotlib.pyplot as plt
import math
import time
import random


# The One-Liner
q = lambda l: q([x for x in l[1:] if x <= l[0]]) + [l[0]] + q([x for x in l if x > l[0]]) if l else []


l = [3, 5, 2, 0, 1, 4]
print(q(l))
# [0, 1, 2, 3, 4, 5]
