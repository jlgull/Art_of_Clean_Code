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


def bubblesortup(lst):
    for passesLeft in range(len(lst)-1, 0, -1):
        for i in range(passesLeft):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

def bubblesortdown(lst):
    for passesLeft in range(len(lst)-1, 0, -1):
        for i in range(passesLeft):
            if lst[i] < lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst


l = [3, 5, 2, 0, 1, 4]
print('\nSorting up ', bubblesortup(l))
# [0, 1, 2, 3, 4, 5]

print('\nSorting down ', bubblesortdown(l))
# [5, 4, 3, 2, 1, 0]