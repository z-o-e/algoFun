'''
# magic index i: A[i]=i
>>> case1 = [-40, -20, -1, 1, 2, 3, 5, 7, 9, 12, 13]
>>> case2 = [-10, -5, 2, 2, 2, 3, 4, 7, 9, 12, 13]
>>> MagicBrute(case1)
7
>>> MagicUniqMain(case1)
7
>>> MagicMutiMain(case2)
[2,7]
'''

def MagicBrute(arr):
    for i in range(len(arr)):
        if arr[i]==i:
            return i
    
    return -1

    
def MagicBisect(arr, start, end):
    # assuming array sorted, magic index unique    
    # similar to binary search approach
    if end < start or start< 0 or end > len(arr)-1:
        return -1
    
    mid = (start+end)//2
    
    if arr[mid]==mid:
        return mid
        
    elif arr[mid] < mid:
        return MagicBisect(arr, mid+1, end)
        
    else:
        return MagicBisect(arr, start, mid-1)


def MagicBisectMulti(arr, start, end, res):
    # asuming array sorted, array elements might have duplicates, 
    # i.e. magic index possibly non-unique
    # search both left, right in recursive calls 
    if end < start or start < 0 or end > len(arr)-1:
        return 
        
    midIdx = (start+end)//2
    midVal = arr[midIdx]
    
    if midIdx==midVal:
        res.append(midIdx)
    
    leftIdx = min(midIdx-1, midVal)
    left = MagicBisect(arr, start, leftIdx)    
    if left>=0:
        res.append(left)
    
    rightIdx = max(midIdx+1, midVal)
    right = MagicBisect(arr, rightIdx, end)
    if right>=0:
        res.append(right)
            

def MagicUniqMain(arr):
    return MagicBisect(arr, 0, len(arr)-1)
    
def MagicMultiMain(arr):
    res = []
    MagicBisectMulti(arr, 0, len(arr)-1, res)
    return res
    
    