import string

class Node:
    def __init__(self):
        d = {}
        for c in string.ascii_lowercase:
            d[c] = None
        self.next = d
        self.val = False

class Rtrie:
    def __init__(self):
        self.root = Node()
        self.N = 0  # number of keys in the trie
    
    def size(self):
        return self.N
        
    def isEmpty(self):
        return self.size==0
    
    # @param node: root
    # @param key: a string
    # @param val: a Boolean
    # @param d: an int
    def putHelper(self, node, key, val, d):
        if not node:
            node = Node()
        if d==len(key):
            if not node.val:
                self.N += 1
            node.val = val
            return node
        c = key[d]
        node.next[c] = self.putHelper(node.next[c],key, val, d+1) 
        return node       

    def put(self, key, val):
        if not val:
            self.delete(key)
        else:
            self.root = self.putHelper(self.root, key, val, 0)
    
    # @param node: a Node
    # @param key: a string
    # @param d: an int
    def getHelper(self,node,key,d):
        if not node:
            return None
        if d==len(key):
            return node 
        c = key[d]
        return self.getHelper(node.next[c], key, d+1)

    def get(self, key):
        node = self.getHelper(self.root, key, 0)
        if not node:
            return None
        return node.val

    def contains(self, key):
        return self.get(key)!=None 

R = Rtrie()
R.put('abc', 'chicky buggie bone')
