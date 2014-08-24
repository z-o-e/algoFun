'''
    Given an infinite number of quarters(25 cents), dimes(10 cents), nickels(5 cents) and pennies(1 cent),
    write code to calculate the number of ways of representing n cents
'''

def nCentsWays(n, denominator):
    # tree-like recursive structure
    if denominator==25:
        nextDemon = 10
    elif denominator==10:
        nextDemon = 5
    elif denominator==5:
        nextDemon = 1
    else:
        return 1
        
    ways = 0
    for i in range(n//denominator):
        ways += nCentsWays(n-i*denominator, nextDemon)
    
    return ways
