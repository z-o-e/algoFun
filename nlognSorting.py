# top-down
def qsort(arr):
    if len(arr)<=1:
        return arr
    return qsort([x for x in arr[1:] if x<arr[0]]) + [arr[0]] + qsort([x for x in arr[1:] if x>=arr[0]])

# generic
class Qsort:
    def __init__(self, arr):
        self.arr = arr

    def qsort(self):
        self._qsort(self.arr, 0, len(self.arr))

    def _qsort(self, arr, l, r):
        if l>=r:
            return
        p = self.partition(arr, l, r)
        self._qsort(arr, l, p-1)
        self._qsort(arr, p+1, r)

    def partition(self,arr,l,r):
        pivot = arr[l]
        i = l+1
        for j in range(l+1, r):
            if arr[j] < pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i-1], arr[l] = arr[l], arr[i-1]
        return i-1

print qsort([3,8,2,5,1,4,7,6])
arr = [3,8,2,5,1,4,7,6]
test0 = Qsort(arr)
test0.qsort()

# top-down
def mergeSort(arr):
    if len(arr)==1:
        return arr

    mid = len(arr)//2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])

    i = j =  0
    aux = []
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            aux.append(left[i])
            i += 1
        else:
            aux.append(right[j])
            j += 1

    if i<len(left):
        aux += left[i:]
    if j<len(right):
        aux += right[j:]

    return aux

class MergeSort:
    def __init__(self, arr):
        self.arr = arr

    def mergesort(self):
        self.arr = self._mergesort(self.arr)

    def _mergesort(self, arr):
        if len(arr)<=1: 
            return arr
        mid = len(arr) /2
        left = self._mergesort(arr[:mid])
        right = self._mergesort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        aux = [] 
        i = j = 0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                aux.append(left[i])
                i += 1
            else:
                aux.append(right[j])
                j += 1

        if i<len(left):
            aux += left[i:]
        if j<len(right):
            aux += right[j:]

        return aux
        
print mergeSort([3,8,2,5,1,4,7,6])
arr = [3,8,2,5,1,4,7,6]
test1 = MergeSort(arr)
test1.mergesort()

class HeapSort:
    def __init__(self, arr):
        self.arr = arr

    def heapsort(self):
        # build heap
        # start from the parent of the last node, upto root
        for start in range((len(self.arr)-1)//2,-1,-1):
            self.heapify(self.arr, start, len(self.arr))

        # extract max,  heapify the rest
        for i in range(len(self.arr)-1, 1 , -1):
            self.arr[i], self.arr[0] = self.arr[0], self.arr[i]
            self.heapify(self.arr, 0, i-1)
          
    def heapify(self, heap, start, end):
        parent = (end-1)//2
        while parent >= start:
            self.siftdown(heap, parent, end)
            parent -= 1

    def siftdown(self,heap, start, end):
        while 2*start+1 < end:
            child = 2*start+1
            swap = start
            if heap[swap]<heap[child]:
                swap = child
            if child+1<len(heap) and heap[child] < heap[child+1]:
                swap = child+1
            if swap!=start:
                heap[start], heap[swap] = heap[swap], heap[start]
                start= swap
            else:
                break

arr = [3,8,2,5,1,4,7,6]
ary = [7, 6, 5, 9, 8, 4, 3, 1, 2 ]
test2 = HeapSort(arr)
test2.heapsort()
test3 = HeapSort(ary)
test3.heapsort()

