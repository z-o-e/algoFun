import collections

# a two-pass algorithm for finding frequent pairs from a large set
# @param bigset: a list of sets
# @param support: a int, the threshold number of baskets that contain the pairs 
class Aprior:
    def __init__(self, bigset, support):
        self.bigset = bigset
        self.support = support
        self.d = collections.defaultdict(int) 
        self.dd = collections.defaultdict(int)
    
    # iterate through the bigset and count all items, only keep those who exceeds support threshold 
    def passOne(self):
        for s in self.bigset:
            for item in s:
                self.d[item]+=1
        origKeys = self.d.keys()
        for key in origKeys:
            if self.d[key]<self.support:
                del self.d[key]
        return self.d.keys()

    # generate all k combinations from a list of elements
    def subset(self, basket, k):
        pairs = []
        if k==0:
            return pairs 
        for i in range(len(basket)):
            if k==1:
                pairs.append([basket[i]])
            else:
                for p in self.subset(basket[i+1:], k-1):
                    pairs.append([basket[i]]+p)
        return pairs

    # return popular paris
    def passTwo(self):
        for basket in self.bigset:
            for pair in self.subset(basket, 2):
                if pair[0] in self.d and pair[1] in self.d:
                    self.dd[(pair[0], pair[1])]+=1
        origKeys = self.dd.keys()
        for key in origKeys:
            if self.dd[key]<self.support:
                del self.dd[key]
        return self.dd.keys()

bigset = [['m','c','b'], ['m','p','j'], ['m','b'], ['c','j'], ['m','p','b'], ['m','c','b','j'], ['c','b','j'], ['b','c']]
test =  Aprior(bigset, 3)
test.passOne()
test.passTwo()
