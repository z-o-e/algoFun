# an example of detecting similarities between columns of a zero-one matrix:
# 1. row indexes are permutated randomly, 
# 2. define minhash func as h(C)=the number of the first (in the permutated order) row in which column C has 1
# 3. use independent hash functions to create signature for each column
# 4. construct signature matrix, whose columns represent the sets and rows represent the minhash values, in order of that column
# Property: the probability (over all permutations of the rows) that h(C1)=H(C2) for example is the same as Jaccard similarity Sim(C1, C2)

import sys
import collections

# generate the k-th permutation of sequence [0, 1, ...,n-1]
# @param n: an int  
# @param k: an int
# @return a permutation list of length n
def permute(n,k,factorial):
    nums = [i for i in range(n)]
    res = []
    #k -= 1
    for i in range(n-1, -1, -1):
        cur = nums[k//factorial]
        res.append(cur)
        nums.remove(cur)
        if i!=0:
            k%=factorial
            factorial/=i
    return res

# generate n!
# @param n: an int
# @return an int
def factorial(n):
    res = 1
    for i in range(1,n+1):
        res*= i
    return res

# calculate Jaccard similarity between columns of a matrix based on minHash
# @param m: a 2d list
# @param ncol1, ncol2: two int representing column index
# @return a float
def minHash0(m, ncol1, ncol2):
    nrow, ncol = len(m), len(m[0])
    f,fm = factorial(nrow), factorial(nrow-1)
    sigM= [[ None for i in range(ncol)] for j in range(f)]

    for i in range(f):
        idx = permute(nrow, i, fm)
        j = 0
        while j < nrow and (None in sigM[i]):
            for k in range(ncol):
                if sigM[i][k]==None and m[idx[j]][k]==1:
                    sigM[i][k]=idx[j]
            j += 1

    a = [sigM[i][ncol1] for i in range(f)]
    b = [sigM[i][ncol2] for i in range(f)]

    return 1.*sum([a[i]==b[i] for i in range(f)])/f


# a good approximation to permutation minhash: pick a number of hash functions; for each column col and each function h_i keep track of the M(i,col) signature value 
# @param m: a 2d list
# @param ncol1, ncol2: two int representing column index
# @return a float
# @param funcs: a list of functions                
def minHash(m, ncol1, ncol2, funcs):
    nrow, nfunc = len(m), len(funcs)
    sig1, sig2 = [sys.maxint for i in range(nfunc)], [sys.maxint for i in range(nfunc)]
    
    for i in range(nrow):
        for j in range(nfunc):
            tmp = funcs[j](i)
            if m[i][ncol1]:
                sig1[j] = min(sig1[j],tmp)
            if m[i][ncol2]:
                sig2[j] = min(sig2[j],tmp)
    
    return 1.*sum([sig1[i]==sig2[i] for i in range(nfunc)])/nfunc


# test0
f = factorial(3-1)
for i in range(6):
    print permute(3, i, f)

# test1
m = [[1,0,1,0], [1,0,0,1], [0,1,0,1], [0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]]
print minHash0(m, 0, 2)
print minHash0(m, 1, 3)
print minHash0(m, 0, 1)

# test2, sketchy
def h(x):   return (x+1)%5
def g(x):   return (2*x+3)%5
funcs = [h, g]
mm = [[1,0],[0,1],[1,1],[1,0],[0,1]]
print minHash(mm,0,1,funcs)
print minHash(m, 0, 2,funcs)
print minHash(m, 1, 3,funcs)
print minHash(m, 0, 1,funcs)


# generate a function that helps tweak locality sensitivity hashing parameters
# @param s: a float representing daccard similarity between two columns of a signature matrix
# @param b: an int representing bucket size
# @param r: an int representing row size of a band
# @returns the probability that identical columns are grouped together 
def LSHparam(self, s, b, r):
        return 1-(1-s**r)**b

# # locality sensitive hashing framework
# class LSH:
#     def __init__(self,s,b,r):
#         self.s = s  # daccard similarity
#         self.b = b  # band size
#         self.r = r  # number of rows in each band
#         self.M = [] # signature matrix
#
#     # generate shorter signatures to represent items of the input
#     def shingling(self, input, ngram):
#         # some operations on self.M
#         self.shingles = collections.defaultdict(int)
#         for i in range(len(input)-ngram):
#             self.shingles[input[i:i+ngram]] += 1         
          
#     # for each band, use minhash to find candidate pairs
#     def minHash(self, funcs):
#         pairs = []
#         for i in range(self.b):
#             for col in self.M[i:(i+1)*self.b]:
#                 # apply some minhash function
#                 # assuming col_j and col_k ended in a same bucket
#                 pairs.append([j,k])
#
#         return pairs
                
