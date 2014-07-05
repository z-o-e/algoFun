#Push all the zero's of a given array to the end of the array. In place only. 
#Ex 1,2,0,4,0,0,8 becomes 1,2,4,8,0,0,0

def zeroback(n):
    idx1,idx2 = 0, len(n)-1
    
    while idx1<=idx2:
        if n[idx1]==0 and n[idx2]!=0:
            n[idx1], n[idx2] = n[idx2], n[idx1]
            idx1+=1
            idx2-=1
        elif n[idx2]==0:
            idx2-=1
        else:
            idx1+=1
    return n

print zeroback([1,2,0,4,0,0,8])
