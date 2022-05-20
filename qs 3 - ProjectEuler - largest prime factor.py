# -*- coding: utf-8 -*-
"""
Created on Wed Mar  3 20:09:03 2021

@author: Y-dee

https://projecteuler.net/problem=3
"""

# how to work out prime factors??

#prime factors of 48
store = []
def primeFactors(number):
    
    for i in range(number-1,0,-1):
        
        if number%i == 0:   # if i is a factor of number
            #print(i)
            store.append(number/i)      # store the divisor
            if i == 1:
                store.append(1)
            else:
                primeFactors(i)             # find the factors of the factor
            return store

def largestPrimeFactors(number):
    store = primeFactors(number)
    
    return max(store)

#start 2013
# end 
#num = 600851475143        
#print(primeFactors(num))
#print(largestPrimeFactors(num))

# VERSION TWO IS MUCH FASTER
# terminates in under 1 second, whilst version 1
# does not terminate

import time

def versionTwo(number):

    start = time.time() 
   
    store = []
    print(number)
    
    def primes(number):
        
        
        if(number == 1):
            store.append(1)
        
        else:
            i = 2
            while number%i !=0:
                i += 1 
                #if number%i ==0:
            store.append(i)
            #print(i)
            primes(number/i)
        
    primes(number)
        
    elapsed = time.time() - start
    print(elapsed)
    
    return store
        
#num2 = 3000000000000
num2 = 600851475143
print(versionTwo(num2))
print(max(versionTwo(num2)))