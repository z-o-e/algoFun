"""
Given an array, remove the duplicates and return a unique array keeping the first occurrence of the duplicates and the order. 

[@2, @1, @3, @1, @2] --> [@2, @1, @3]
"""

def removeDup(arr):
    res = []
    bag = {}
    for i in arr:
        if i not in bag:
            bag[i] = 1
            res.append(i)
    return res
    
print removeDup(['@2', '@1', '@3', '@1', '@2'])