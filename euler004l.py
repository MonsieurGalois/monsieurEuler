# -*- coding: utf-8 -*-
'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

import time
a=time.time()
numbers=[]
for i in range(999,99,-1):
    for z in range(i,99,-1):
        e=z*i
        N=str(e)
        NN=N[::-1]
        if N==NN:
            numbers.append(e)
print max(numbers)
b=time.time()
print b-a
