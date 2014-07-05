#If a=1, b=2, c=3,....z=26. Given a string, find all possible codes that string can generate. Give a count as well as print the strings. 
#
#For example: 
#Input: "1123". You need to general all valid alphabet codes from this string. 
#
#Output List 
#aabc //a = 1, a = 1, b = 2, c = 3 
#kbc // since k is 11, b = 2, c= 3 
#alc // a = 1, l = 12, c = 3 
#aaw // a= 1, a =1, w= 23 
#kw // k = 11, w = 23

import string

def convert(n):
    d = {}
    letters = string.lowercase
    
    for i in range(1,27,1):
        d[str(i)] = letters[i-1]
        
    res = []
    tmp = cur = ""
    if len(n)>1 and int(n[:2])<27:
        tmp += d[n[:2]]
        res = dfs(n[2:], res, tmp, d)
    
        
    cur += d[n[0]]
    res = dfs(n[1:], res, cur, d)
    
    return res
    
def dfs(currentString, res, currentWord, dictionary ):  
    
    if currentString=='':
        if currentWord not in res:
            res.append(currentWord)
        return res
        
    tmp = currentWord
    if len(currentString)>1 and int(currentString[:2])<27:
        tmp += dictionary[currentString[:2]]
        res = dfs(currentString[2:], res, tmp, dictionary)
        
    currentWord += dictionary[currentString[0]]
    res = dfs(currentString[1:], res, currentWord, dictionary)
    
    return res
    
print convert('1123')
