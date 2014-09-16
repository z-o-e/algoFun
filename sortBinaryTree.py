# Given a Binary Tree, convert it to a Binary Search Tree.
# The conversion must be done in such a way that keeps the original structure.

def sortBT(root):
    origRoot = root
    vals, stack = [], []
    if root==None:
        return root
    
    # inorder traversal record node vals    
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            vals.append(root.val)
            root = root.right
            
    # sort node vals desc
    vals = sorted(vals, reverse=True)
    
    # inorder traversal record node vals
    stack = []
    root = origRoot
    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            root = stack.pop()
            root.val = vals.pop()
            root = root.right
    
    return origRoot    