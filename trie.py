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
    # @param val
    # @param d: an int
    def _put(self, node, key, val, d):
        if not node:
            node = Node()
        if d==len(key):
            if not node.val:
                self.N += 1
            node.val = val
            return node
        c = key[d]
        node.next[c] = self._put(node.next[c],key, val, d+1) 
        return node       
    
    # @param key: a string
    # @param val
    def put(self, key, val):
        if not val:
            self.delete(key)
        else:
            self.root = self._put(self.root, key, val, 0)
    
    # @param node: a Node
    # @param key: a string
    # @param d: an int
    def _get(self,node,key,d):
        if not node:
            return None
        if d==len(key):
            return node 
        c = key[d]
        return self._get(node.next[c], key, d+1)

    # @param key: a string
    def get(self, key):
        node = self._get(self.root, key, 0)
        if not node:
            return None
        return node.val
    
    # @param key: a string
    def contains(self, key):
        return self.get(key)!=None 
    
    # @param prefix: a string
    def keysWithPrefix(self, prefix):
        res = []
        node = self.get(self.root, prefix, 0)
        self._collect(node, prefix, res)
        return res
        
    # @param node: a Node    
    # @param prefix: a string
    # @param res: a list
    def _collect(self, node, prefix, res):
        if not node:
            return 
        if node.val:
            res.append(prefix)
        for c in string.ascii_lowercase:
            self._collect(node.next[c], prefix+c, res)
    
    # @param pattern: a string
    def keysThatMatch(self, pattern):
        res = []
        self._collect2(self.root, '', pattern, res)
        return res

    # @param node: a Node    
    # @param prefix: a string
    # @param pattern: a string
    # @param res: a list
    def _collect2(self, node, prefix, pattern, res):
        if not node:
            return 
        d = len(prefix)
        if d==len(pattern) and node.val:
            res.append(prefix)
        if d==len(pattern):
            return
        c = pattern[d]
        if c=='.':
            for ch in string.ascii_lowercase:
                self._collect2(node.next[ch], prefix+'ch', res)
        else:
            self._collect2(node.next[c], prefix+'ch', res)
    
    # @param key: a string    
    def delete(self, key):
        self.root = self.delete(self.root, key, 0)

    # @param node: a Node    
    # @param key: a string
    # @param d: an int
    def _delete(self, node, key, d):
        if not Node:
            return None
        if d==len(key):
            if node.val:
                self.N-=1
        else:
            c = key[d]
            x.next[c] = self._delete(x.next[c], key, d+1)
        
        # remove subtrie rooted at node if it is completely empty
        if node.val:
            return node
        for c in string.ascii_lowercase:
            if node.next[c]:
                return node
        return None

R = Rtrie()
R.put('abc', 'chicky buggie bone')
