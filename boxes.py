'''
    You have a stack of n boxes, with width w_i, height h_i and depth d_i.
    The boxes cannnot be rotated and can only be stacked on top of one another
    if each box in the stack is strictly larget than the box above it 
    in width, height and height.
    Implement a method to build the tallest stack possible, 
    where the hight of a stack is the sum of the heights of each box.
'''

class box:
    def __init__(self, w, h, d):
        self.w = w
        self.h = h
        self.d = d

def createStack(boxes, bottom):
    # a recursive approach with redundancy
    maxHeight = 0
    
    maxStack = []
    
    for i in range(len(boxes)):
        if boxes[i].w<bottom.w and boxes[i].h<bottom.h and boxes[i].d<bottom.d:
            newStack = createStack(boxes, boxes[i])
            newHeight = sum([b.h for b in newStack])
            if newHeight > maxHeight:
                maxStack = newStack
                maxHeight = newHeight
    
    # no more stacking
    if maxStack==[]:
        maxStack = []
    
    # insert at the bottom of the current maxStack    
    if bottom!=None:
        maxStack = [bottom]+maxStack
        
    return maxStack
    
def createStackDP(boxes, bottom, stackMap):
    # use stackMap to record previously found maxStack  
    if bottom!=None and bottom in stackMap:
        return stackMap[bottom]
        
    maxHeight = 0
    maxStack = []
    
    for i in range(len(boxes)):
        if boxes[i].w<bottom.w and boxes[i].h<bottom.h and boxes[i].d<bottom.d:
            newStack = createStackDP(boxes, boxes[i], stackMap)
            newHeight = sum([b.h for b in newStack])
            if newHeight > maxHeight:
                maxStack = newStack
                maxHeight = newHeight
            
    if maxStack==[]:
        maxStack = []
    
    if bottom!=None:
        maxStack = [bottom]+maxStack
        
    stackMap[bottom] = maxStack
    
    return maxStack
    