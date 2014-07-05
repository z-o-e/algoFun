"""
Input - List<String> ["star", "rats", "ice", "cie", "arts"] 
print all anagrams in buckets: 
["star", "rats", "arts"] 
["ice", "cie"] 
"""

def anagrams(L):
    
    D = {}
    for item in L:
        itemSorted = ''.join(sorted(item))
        if itemSorted in D:
            D[itemSorted].append(item)
        else:
            D[itemSorted] = [item]
            
    for key in D:
        print key, D[key]
        
anagrams(["star", "rats", "ice", "cie", "arts"])