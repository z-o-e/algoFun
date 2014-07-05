"""
Code a function that receives a string composed by words separated by spaces and returns a string where words appear in the same order but than the original string, but every word is inverted. 
Example, for this input string


@"the boy ran"
the output would be


@"eht yob nar"
Tell the complexity of the solution.
"""

def reverseWords(s):
    s = s.split(" ")
    
    res = ""
    for word in s:

        for i in range(len(word)-1,-1,-1):
            res += word[i]
            
        res += " "
        
    return res.strip(" ")
    
print reverseWords("the boy ran")
