#A k-palindrome is a string which transforms into a palindrome on removing at most k characters. 
#
#Given a string S, and an interger K, print "YES" if S is a k-palindrome; otherwise print "NO". 
#Constraints: 
#S has at most 20,000 characters. 
#0<=k<=30 
#
#Sample Test Case#1: 
#Input - abxa 1 
#Output - YES 
#Sample Test Case#2: 
#Input - abdxa 1 
#Output - No

def kpalindrome(s, k):
    l = len(s)
    
    
    distTable = [[0 for i in range(l+1)] for i in range(l+1)]
    distTable[0] = [i for i in range(l+1)]
    for i in range(1,l+1, 1):
        distTable[i][0] = i

    
    for i in range(1,l+1,1):
        for j in range(1,l+1,1):
            if s[i-1]== s[l-1-(j-1)]:
                distTable[i][j] = distTable[i-1][j-1]
            else:
                distTable[i][j] = min(distTable[i-1][j-1]+2, distTable[i-1][j]+1, distTable[i][j-1]+1)

    if distTable[l][l]/2 <= k:
        return "YES"
    return "NO"

print kpalindrome("abxa" ,1)
print kpalindrome("abdxa", 1)