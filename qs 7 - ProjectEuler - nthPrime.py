# -*- coding: utf-8 -*-
"""
Created on Thu Mar  4 06:17:03 2021

@author: Y-dee
"""

def nthPrime(number):
    
    store = [2]
    
    if number == 1:
       return store
    else:    
        count = 2
        i = 0
        while len(store) < number:  #only stop when the length of the number of primes == number of primes one wants
            while i < len(store):
                print('entering count is ' + str(count))
                print(str(count) + '%'+ str(store[i])+' ' +str(count%store[i]))

                if count%(store[i]) == 0:
                    print('count mod ' +str(count%store[i]))
                    print(count)
                    print('i is '+ str(i))
                    count += 1  # move to next prospective number
                    i = 0      #go back to first prime
                    #break #--> this caused error
                
                print(store)
                print('i is '+ str(i))

                    
            # if make it through for loop, then a prime number
            store.append(count)
            count +=1
                
        return store
                    
#ans = nthPrime(7)
#print(ans)
#print(max(ans))

def versionTwo(number):
    
    counter = 3
    store = [2]
    
    if number == 0 or number ==1:
        return []
    elif number == 2:
        return store
    
    else: 
        
        i = 0 
        while len(store)< number:
            if counter%store[i] != 0  and i == len(store)-1:
                # final prime found
                store.append(counter)
            elif counter%store[i]!= 0:
                i += 1
            else:
                i = 0
                counter += 1
    
                    
    return store

#print(versionTwo(100))
#print(versionTwo(200))
#ans = versionTwo(10001)
ans = versionTwo(10000)
print(ans)
print(max(ans))