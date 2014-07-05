"""
Write a function that takes a string and returns true if the entire string is a palindrome, otherwise return false. The function should be case-insensitive and ignore any whitespace or punctuation. 

For example, return true for: 
\"A man, a plan, a canal: Panama.\"
"""

def palindrome(s):
    ss = ""
    for i in s:
        if (i<="Z" and i>="A"):
            ss += i.lower()
        elif (i<="z" and i>="a"):
            ss += i
    
    idx1, idx2 = 0, len(ss)-1
    while idx1<idx2:
        if ss[idx1]==ss[idx2]:
            idx1+=1
            idx2-=1
        else:
            return False
            
    return True
    
print palindrome("A man, a plan, a canal: Panama.")
            