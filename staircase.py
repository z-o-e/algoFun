'''
    A child is running up a staircase with n steps, and can hop either 1 step, 2 steps, or 3 steps at a time. 
    Implement a method to count how many possible ways the child can run up the stairs.
'''

def countWaysExponential(n):
    # a naive implementation using recursion takses O(3^n)
    if n<0:
        return 0
    if n==0:
        return 1
    
    return countWaysExponential(n-1)+countWaysExponential(n-2)+countWaysExponential(n-3)
    
def countWaysDP(n):
    # a dp solution of using recursion with caching is O(n)
    if n<0:
        return 0

    elif n==0:
        return 1

    elif map[n]>-1:
        return map[n]
        
    else:
        map[n] = countWaysDP(n-1) + countWaysDP(n-2) + countWaysDP(n-3)
        
        return map[n]
    
    