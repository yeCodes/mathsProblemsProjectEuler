# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 04:01:57 2021

@author: Y-dee
https://projecteuler.net/problem=6
"""

def sumSquareDifference(number):
    
    val = 0 
    product = 0
    
    for i in range (1, number +1):
        #print(i)
        val += i
        product += pow(i,2)
        
    #print(product)
    return abs(product - pow(val,2))

print(sumSquareDifference(100))
