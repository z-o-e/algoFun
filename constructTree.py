"""
given a sorted (increasing order) array, 
write an algorithm to create a binary search tree with minimal height
"""

def recur(arr, startIdx, endIndx):
    if endIndx<startIdx:
        return 
    
    midIdx = (startIdx + endIndx)/2
    r = TreeNode(arr[midIdx])
    r.left = recur(arr, startIdx, midIdx-1)
    r.right = recur(arr, midIdx+1, endIndx)
    
    return r
    
def createMinimalBST(arr):
    return recur(arr, 0, len(arr)-1)

