#Power set P(S) of a set S is the set of all subsets of S. For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}. 
#If S has n elements in it then P(s) will have 2^n elements
"""
>>> S = ['a','b','c']
>>> P(S)
 [[], [a], [b], [c], [a,b], [a, c], [b, c], [a, b, c]]
"""

def P(S):
    s = sorted(S)
    res, cur = [], []
    depth, sLen = 0, len(S)
    
    helper(res, cur, depth, sLen, s)
    
    return res
    
def helper(res, cur, depth, sLen, s):
    res.append(cur)
    
    if depth==sLen:
        return
        
    for i in range(depth, sLen):
        tmp = cur[:]
        tmp.append(s[i])
        helper(res, tmp, i+1, sLen, s)

