# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 19:57:01 2021

@author: Y-dee
"""

# generate fibonacci numbers, bounded < 4millions
# sum even terms
# only sum if even

fib0 = 1
fib1 = 2

fibn = 0
sum = 0

while fibn <= 4e6:
    
    fibn = fib1 + fib0
    fib0 = fib1
    fib1 = fibn
    
    if fibn%2 == 0:
        sum += fibn
        
print(sum)
