# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:35:35 2021

@author: Y-dee
https://projecteuler.net/problem=5
"""

import math

def smallestMultiple():
    
        number = 1
      
        i = 1
        while i <= 20:
            print(number)
            if number % i == 0:
                i += 1
            else:
                number+=1
                i = 1
                #break
        return number

#slow approach!!
#print(smallestMultiple())

def versionTwo():
    
    i = 1
    product = 1
    while i <= 20:
        product = product*i
        i += 1
    
    return product

print(versionTwo())
print(math.factorial(20))