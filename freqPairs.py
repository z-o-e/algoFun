import collection

# two implementations of finding and getting frequent pairs
# @param pairs: a list of pair tuples
# @param n: an int of total number of items
class FreqPair:
    def __init__(self,pairs, n):
        # keep pairs sorted and suppose the values are hashed to int
        self.pairs = sorted(self.pairs, key=lambda x:(x[0], x[1]))
        self.n = n

    def matrixFind(self):
        # flattened triangular matrix, about 2n^2 bytes in total
        self.matrix = [0]*n*(n-1)/2
               for p in pairs:
            i,j = p[0],p[1]    
            # simple recipe [i,j] is in position (i-1)*(n-i/2)+j-i of self.matrix
            self.matrix[(i-1)*(n-i/2)+j-i] += 1
        return self.matrix

    def matrixGet(self, i, j):
        try:
            return self.matrix[(i-1)*(n-i/2)+j-i]
        except:
            return 'triangular matrix not initiated, or either at least one of '+str(i)+' and '+str(j)' not existant'
    
    def tabularFind(self):
        # hash table, 12p bytes, where p is the number of pairs, which beats matrixFind if at most 1/3 of the possible pairs occur
        self.table = collections.defaultdict(int) 
        for p in self.pairs:
            self.table[p] += 1
        return self.table

    def tabularGet(self, i, j):
        try:
            return self.table[[i,j]]
        except:
            return 'no such pair'         
