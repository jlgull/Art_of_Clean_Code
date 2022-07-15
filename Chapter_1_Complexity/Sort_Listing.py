#! / bin / python3
#
# Author: Jonathan Heard
# Work from 'Art of Clean Code'
#
# Program name: Sort_Analysis.py
#

""" Import all the needed external methods """
import matplotlib.pyplot as plt
import math
import time
import random


def bubblesort(l):
    # src: https://blog.finxter.com/daily-python-puzzle-bubble-sort/
    lst = l[:] # Work with a copy, don't modify the original
    for passesLeft in range(len(lst)-1, 0, -1):
        for i in range(passesLeft):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def qsort(lst):
    # Explanation: https://blog.finxter.com/python-one-line-quicksort/
    q = lambda lst: q([x for x in lst[1:] if x <= lst[0]])
                    + [lst[0]]
                    + q([x for x in lst if x > lst[0]]) if lst else []
    return q(lst)


