# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 21:29:18 2021

@author: Y-dee
https://projecteuler.net/problem=4
"""

productMax = 0
storeOne = 0
storeTwo = 0

for i in range (999,99,-1):
    for j in range(999,99,-1):
        product = i * j
        
        num = str(product) 
        reverseNum = num[::-1]
        
        # if product is larger than what has been observed
        # AND number is a palindrome, update the max product
        if product > productMax and num == reverseNum:
            productMax = product
            storeOne, storeTwo = i, j

print(storeOne)
print(storeTwo)
print(productMax)