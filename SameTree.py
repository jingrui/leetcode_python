# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param p, a tree node
    # @param q, a tree node
    # @return a boolean
    def isSameTree(self, p, q):
        def check(p,q):
            if p == None and q == None:     return True
            elif p == None or q == None:    return False
            elif p.val == q.val:
                return check(p.left,q.left) and check(p.right,q.right)
            else:
                return False
        return check(p,q)
        
