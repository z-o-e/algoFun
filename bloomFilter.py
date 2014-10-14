# bloom filter is a space-efficient probabilistic data structure to check whether an element is a member of a very large set. 
# False positive are possible, false negative are impossible (100% recall)
# probability of a false positive depends on the density of 1's in the array and the number of hash functions
# (the number of 1's is approximately the number of elements inserted times the number of hash functions)
# suppose bitArraySize: b, hashFunctionSize: h, streaElementSize: n
# throwing d darts at t targets at random: (1-1/t)^d = (1-1/t)^(t*d/t) ~= e^(-d/t) 
# for example: suppose b=1b, h=5, n=100m, that is t = 10^9, d = 5*10^8
# the fraction of 0's e^(-1/2), fraction of 1's: 1-e^(-1/2), fraction of false positive (1-e^(-1/2))^5

import math

# @param funcs: a list of hash functions
# @param filterSize: an int representing the size of bloom filter -- a bit vector
class bloomFilter:
    def __init__(self, funcs, filterSize):
        self.funcs = funcs
        self.bitArray = [0]*filterSize

    def _dec2Binary(self, dec):
        if dec==0:
            return [0]
        res = []
        while dec:
            res = [dec%2] + res
            dec //= 2
        return res
    
    def set(self, streamElem):
        elem = self._dec2Binary(streamElem)
        for func in self.funcs:
            idx = func(elem, len(self.bitArray))
            self.bitArray[idx] |= 1 
            
    def lookup(self, newElem):
        elem = self._dec2Binary(newElem)
        for func in self.funcs:
            idx = func(elem, len(self.bitArray))
            if self.bitArray[idx]==0:
                return False
        return True

    def estimateFP(self,streamSize):
        zeros = math.exp(-len(self.funcs)*streamSize/len(self.bitArray))
        fp =  (1-zeros)**(len(self.funcs))
        return fp        


# h1, h2 take odd-numbered, even-numbered bits startinf from the right of binary representation of x
def h1(x,modula):
    odds = []
    for i in range(len(x)-1,-1,-2):
        odds = [x[i]]+odds
    res = 0
    i = 0
    while odds:
        t = odds.pop()
        if t==1:
            res += 2**i
        i+=1
    return res%modula

def h2(x,modula):
    evens = []
    for i in range(len(x)-2,-1,-2):
        evens = [x[i]]+evens
    res = 0
    i = 0
    while evens:
        t = evens.pop()
        if t==1:
            res += 2**i
        i+=1
    return res%modula
            
funcs = [h1, h2]
filterSize = 11
test = bloomFilter(funcs, filterSize)
test.set(25)
test.set(159)
test.lookup(25)
test.lookup(159)
test.lookup(30)
test.bitArray
