#Given a function 
#
#getRandomTripplet() 
#
#which returns a random triplet of letters from a string. You don't know the string using calls to this function you have to correctly guess the string. the length of the string is also given. 
#
#Lets say the string is helloworld the function getRandomTriplet will return things like 
#
#hlo 
#hew 
#wld 
#owo 
#
#the function maintains the relative order of the letters. so it will never return 
#
#ohl since h is before o in the string. 
#owe since w is after e 
#
#The string is not known you are only given length of the string.

import random

def getRandomTripplet(S):
    idx = sorted(random.sample(range(len(S)), 3))
    
    res = ''
    for i in idx:
        res+=S[i]
        
    return res
    
S = "helloworld"    
print getRandomTripplet(S)
    