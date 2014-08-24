'''
    unique path from board(0,0) to board(X,Y) with off-limit spots
'''

def isFree(x,y):
    if board[x,y]!=-1:
        return True
        
    return False


def getPath( x, y, path, cache):
    # use array list to record path
    # array dict cache to store current spots avoiding duplicates
    if [x,y] in cache:
        return cache[[x,y]]
        
    path.append([x,y])
    
    if x==0 and y==0:
        return True
    
    success=False
    
    if x>=1 and isFree(x-1, y):
        success = getPath(x-1, y, path, cache)
        
    if not success and y>=1 and isFree(x, y-1):
        success = getPath(x, y-1, path, cache)
    
    if not success:
        path.remove([x,y])
        
    cache[[x,y]] = True
    
    return success
    
    
def solvePath(board, X, Y):
    return getPath(X, Y, [], {})       
        
    