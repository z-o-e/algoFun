# Given that integers are read from a data stream. Find median of elements read so for in efficient way.
# For simplicity assume there are no duplicates. For example, let us consider the stream 5, 15, 1, 3 and so on
#
# After reading 1st element of stream - 5 -> median - 5
# After reading 2nd element of stream - 5, 15 -> median - 10
# After reading 3rd element of stream - 5, 15, 1 -> median - 5
# After reading 4th element of stream - 5, 15, 1, 3 -> median - 4, so on

class heap():
    def __init__(self,heapType):
        self.heap = []
        if heapType in ('min','max'):
            self.heapType = heapType
        else:
            return 'invalid heap type'
        
    def getSize(self):
        return len(self.heap)
        
    def getTop(self):
        return self.heap[0]
        
    def heapify(self, newElem):
        if not self.heap:
            self.heap = [newElem]
        # append to the end
        self.heap.append(newElem)
        i = len(self.heap)-1
        
        # bubble up
        if self.heapType=='min':
            while i>0 and self.heap[i]<self.heap[(i-1)//2]:
                self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                i = (i-1)//2
        if self.heapType=='max':
            while i>0 and self.heap[i]>self.heap[(i-1)//2]:
                self.heap[i], self.heap[(i-1)//2] = self.heap[(i-1)//2], self.heap[i]
                i = (i-1)//2           
        
    def extractM(self):
        if not self.heap:
            return None
        # min or max
        res = self.heap[0]
        if len(self.heap)<3:
            self.heap = self.heap[1:]
            return res
            
        # swap root and last element    
        self.heap[0],self.heap[-1] = self.heap[-1], self.heap[0]
        self.heap = self.heap[:-1]
        
        i = 0
        if self.heapType=='min':
            while 2*i+1<len(self.heap):
                if 2*i+2<len(self.heap):
                    if self.heap[i] < self.heap[2*i+2] and self.heap[i] < self.heap[2*i+1]:
                        break
                    elif self.heap[2*i+2]< self.heap[2*i+1]:
                        self.heap[i], self.heap[2*i+2] = self.heap[2*i+2], self.heap[i]
                        i = 2*i+2
                    else:
                        self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                        i = 2*i+1
                else:
                    if self.heap[i] < self.heap[2*i+1]:
                        break
                    else:
                        self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                        i = 2*i+1
                    
        if self.heapType=='max':
            while 2*i+1<len(self.heap):
                if 2*i+2<len(self.heap):
                    if self.heap[i] > self.heap[2*i+2] and self.heap[i] > self.heap[2*i+1]:
                        break
                    elif self.heap[2*i+2] > self.heap[2*i+1]:
                        self.heap[i], self.heap[2*i+2] = self.heap[2*i+2], self.heap[i]
                        i = 2*i+2
                    else:
                        self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                        i = 2*i+1
                else:
                    if self.heap[i] > self.heap[2*i+1]:
                        break
                    else:
                        self.heap[i], self.heap[2*i+1] = self.heap[2*i+1], self.heap[i]
                        i = 2*i+1
        
        return res

class medStream():
    def __init__(self):
        self.maxHeap = heap('max')
        self.minHeap = heap('min')

    # maxHeap maintains the lower half of the nums, minHeap maintains the greater half
    def getMed(self, newNum):
        if not self.maxHeap.heap and not self.minHeap.heap:
            self.maxHeap.heapify(newNum)
            return newNum
    
        if self.maxHeap.getSize()==1 and not self.minHeap.heap:
            if self.maxHeap.getTop()>newNum:
                self.minHeap.heapify(self.maxHeap.extractM())
                self.maxHeap.heapify(newNum)
            else:
                self.minHeap.heapify(newNum)
        else:    
            if newNum>self.maxHeap.getTop() and newNum<self.minHeap.getTop():
                if self.maxHeap.getSize()<self.minHeap.getSize():
                    self.maxHeap.heapify(newNum)
                else:
                    self.minHeap.heapify(newNum)
                return newNum
            elif newNum<self.maxHeap.getTop():
                self.maxHeap.heapify(newNum)
            else:
                self.minHeap.heapify(newNum)
        
        sizeDiff = self.maxHeap.getSize()-self.minHeap.getSize()
        if sizeDiff==0:
            return (self.maxHeap.getTop()+self.minHeap.getTop())/2.
        if sizeDiff==-1:
            return self.minHeap.getTop()
        if sizeDiff==1:
            return self.maxHeap.getTop() 
        
        # resize two heaps   
        if sizeDiff<-1:
            self.maxHeap.heapify(self.minHeap.extractM())
        elif sizeDiff>1:
            self.minHeap.heapify(self.maxHeap.extractM())
        return (self.maxHeap.getTop()+self.minHeap.getTop())/2.

test = medStream()
for elem in [5, 15, 1, 3]:
    print test.getMed(elem)
           
