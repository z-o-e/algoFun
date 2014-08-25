'''
    You are given two 32-bit numbers, N and M, and bit positions, i and j. 
    Write a method to insert M into N such that M starts at bit j and ends at bit i. 
    You can assume that the bits j through i have enough space to fit all of M. 
    That is, if M = 10011, you can assume that there are at least 5 bits between j and i. 
    You would not, for example, have j = 3 and i = 2, because M could not fully fit between bit 3 and bit 2.
    EXAMPLE:
        Input: N = 10000000000, M = 10011, i = 2, j = 6
        Output: N = 10001001100

        1. set N from i to j to 0.
        2. shift M
        3. merge
'''

def updateBits(N, M , i ,j):
    left = ~0 << (j+1)
    right = (1<<i)-1    
    mask = left | right
    
    NCleared = N & mask
    MShifted = M << i   
    
    return NCleared | MShifted, bin(NCleared | MShifted)
