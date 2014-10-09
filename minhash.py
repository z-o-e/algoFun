# an example of detecting similarities between columns of a zero-one matrix:
# 1. row indexes are permutated randomly, 
# 2. define minhash func as h(C)=the number of the first (in the permutated order) row in which column C has 1
# 3. use independent hash functions to create signature for each column
# 4. construct signature matrix, whose columns represent the sets and rows represent the minhash values, in order of that column
# Property: the probability (over all permutations of the rows) that h(C1)=H(C2) for example is the same as Jaccard similarity Sim(C1, C2)

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
                 

# test0
f = factorial(3-1)
for i in range(6):
    print permute(3, i, f)

# test1
m = [[1,0,1,0], [1,0,0,1], [0,1,0,1], [0,1,0,1],[0,1,0,1],[1,0,1,0],[1,0,1,0]]
print minHash0(m, 0, 2)
print minHash0(m, 1, 3)
print minHash0(m, 0, 1)
