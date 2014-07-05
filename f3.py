#String Reduction 
#
#Given a string consisting of a,b and c's, we can perform the following operation: Take any two adjacent distinct characters and replace it with the third character. For example, if 'a' and 'c' are adjacent, they can replaced with 'b'. What is the smallest string which can result by applying this operation repeatedly? 
#
#Input: 
#The first line contains the number of test cases T. T test cases follow. Each case contains the string you start with. 
#
#Output: 
#Output T lines, one for each test case containing the smallest length of the resultant string after applying the operations optimally. 
#
#Constraints: 
#1 <= T <= 100 
#The string will have at most 100 characters. 
#
#Sample Input: 
#3 
#cab 
#bcab 
#ccccc 
#
#Sample Output: 
#2 
#1 
#5 
#
#Explanation: 
#For the first case, you can either get cab -> cc or cab -> bb, resulting in a string of length 2. 
#For the second case, one optimal solution is: bcab -> aab -> ac -> b. No more operations can be applied and the resultant string has length 1. 
#For the third case, no operations can be performed and so the answer is 5.

def count(s):
    chars = 'abc'
    l = len(s)
    
    if l>1 and s.count(s[0])!=len(s):
        if s[0]!=s[1]:
            replace = chars.strip(s[:2])
            s = replace+s[2:]
            l -= 1
            l = rec(s,l,chars)
        else:
            s = s[1:]
            l = rec(s,l,chars)
            
    return l

def rec(s, l, chars):
    if s<2:
        return l
    
    while l>1 and s.count(s[0])!=len(s):
        if s[0]!=s[1]:
            replace = chars.strip(s[:2])
            s = replace + s[2:]
            l-=1
            l = rec(s,l,chars)
        else:
            s = s[1:]
            l = rec(s,l,chars)
            
    return l

test = ['cab', 'bcab', 'ccccc']
for t in test:   
    print count(t)
        