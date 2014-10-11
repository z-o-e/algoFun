import collections

# two implementations of finding and getting frequent pairs, useful component for association analysis
# @param pairs: a list of pair tuples
# @param n: an int of total number of items
class FreqPair:
    def __init__(self,pairs, n):
        # keep pairs sorted and suppose the values are hashed to int
        self.pairs = [tuple(sorted((p[0],p[1]))) for p in pairs] 
        self.n = n

    def matrixFind(self):
        # flattened triangular matrix, about 2n^2 bytes in total
        self.matrix = [0]*(self.n*(self.n-1)/2)
        for p in self.pairs:
            i,j = p[0],p[1]    
            # simple recipe [i,j] is in position i*(n-(i+1)/2)+j-i-1 of zero-indexing self.matrix
            self.matrix[i*(n-(i+1)/2)+j-i-1] += 1
        return self.matrix

    def matrixGet(self, i, j):
        if i>j:
            i,j = j,i
        try:
            return self.matrix[i*(n-(i+1)/2)+j-i-1]
        except:
            return 'triangular matrix not initiated, or either at least one of '+str(i)+' and '+str(j)+' not existant'
    
    def tabularFind(self):
        # hash table, 12p bytes, where p is the number of pairs, which beats matrixFind if at most 1/3 of the possible pairs occur
        self.table = collections.defaultdict(int) 
        for p in self.pairs:
            self.table[p] += 1
        return self.table

    def tabularGet(self, i, j):
        if i>j:
            i,j = j,i
        try:
            return self.table[(i,j)]
        except:
            return 'no such pair'        

pairs = [[0,1],[0,2],[0,3],[1,2],[1,3],[3,4],[2,1]]
n = 5
test = FreqPair(pairs, n)
test.matrixFind()
test.matrixGet(0,1)
test.matrixGet(2,3)
test.tabularFind()
test.tabularGet(1,2)
test.tabularGet(1,4)
 
