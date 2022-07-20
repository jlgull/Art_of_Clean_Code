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
    q = lambda lst: q([x for x in lst[1:] if x <= lst[0]]) + [lst[0]] + q([x for x in lst if x > lst[0]]) if lst else []
    return q(lst)

def timsort(l):
    # sorted() uses Timsort internally
    return sorted(l)

def create_random_list(n):
    return random.sample(range(n), n)

n = 5000
xs = list(range(1,n+n//100,n//10))
y_bubble = []
y_qsort = []
y_tim = []

for x in xs:
    # Create list
    lst = create_random_list(x)

    # Measure time bubble sort
    start = time.time()
    bubblesort(lst)
    y_bubble.append(time.time()-start)

    # Measure time qsort
    start = time.time()
    qsort(lst)
    y_qsort.append(time.time()-start)

    # Measure time Timsort
    start = time.time()
    timsort(lst)
    y_tim.append(time.time()-start)

plt.plot(xs, y_bubble, '-x', label='Bubblesort')
plt.plot(xs, y_qsort, '-o', label='Quicksort')
plt.plot(xs, y_tim, '--.', label='Timsort')
plt.grid()

plt.xlabel('List Size (No. Elements)')
plt.ylabel('Runtime (s)')

plt.legend()
plt.savefig('alg_complexity_new.pdf')
plt.savefig('alg_complexity_new.jpg')
plt.show()
