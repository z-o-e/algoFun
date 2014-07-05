#Given - a number (n) and a sorted array 
#Find a number in the array having least difference with the given number (n).

def leastDiff(n, arr):
    if len(arr) == 1:
        return arr[0]
        
    if n<arr[0]:
        return arr[0]
    
    if n>arr[-1]:
        return arr[-1]
   
    low, high = 0, len(arr)-1
    mid = (low+high)/2
    
    while low<=high:    
        if n==arr[mid]:
            return arr[mid]
        elif n>arr[mid]:
            low = mid+1
        else:
            high = mid-1
        mid = (low+high)/2
    
    print low, high
    if abs(arr[low]-n) <= abs(arr[high]-n):
        return arr[low]
    else:
        return arr[high]
        
print leastDiff(25, [10,20,30,40,50])
    