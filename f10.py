"""
Given a list of words, L, that are all the same length, and a string, S, 
find the starting position of the substring of S that is a concatenation of each word in L exactly once and without any intervening characters. 
This substring will occur exactly once in S.
Example: 

L: "fooo", "barr", "wing", "ding", "wing". 

S: "lingmindraboofooowingdingbarrwingmonkeypoundcake". 

fooowingdingbarrwing.
"""

def findConcate(L,S):
    
    wL = len(L[0])
    totalL = len(L)*wL
    
    for i in range(0,len(S)-totalL):

        if S[i:i+wL] in L:
            tmp, searchL = [], totalL
            for w in L:
                if w!=S[i:i+wL]:
                    tmp.append(w)    
            if recur(tmp,S[i+wL:]):
                return S[i:i+totalL]
                
    return S[i:i+totalL]
            
            
def recur(L,S):
    if not L:
        return True
        
    wL = len(L[0])
    if S[:wL] in L:
        tmp = []
        for w in L:
            if w!= S[:wL]:
                tmp.append(w)
        return recur(tmp, S[wL:])
    
    return False
    
print findConcate(["fooo", "barr", "wing", "ding", "wing"], "lingmindraboofooowingdingbarrwingmonkeypoundcake")
         