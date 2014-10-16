#Given three corner points of a triangle, and one more point P. 
#Check whether P lies within the triangle or not.

# @param a,b,c, three (x, y) tuples of points
# @return a float
def area(a,b,c):
    # based on Heron's formula:
    return abs(a[0]*(b[1]-c[1])+b[0]*(c[1]-a[1])+c[0](a[1]-b[1]))/2.

# @param a,b,c, three (x, y) tuples of points
def isInside(a,b,c, newElem):
    A = area(a,b,c)
    a1 = area(newElem, b, c)
    a2 = area(a, newElem, c)
    a3 = area(a, b, newElem)
    
    return A==(a1+a2+a3)
