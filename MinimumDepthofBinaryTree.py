# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def minDepth(self, root):
        def helper(node):
            if node == None:
                return 0
            if node.left == None and node.right == None:
                return 1
            
            cands = []
            lret = helper(node.left)
            rret = helper(node.right)
            if lret != 0:
                cands.append(lret)
            if rret != 0:
                cands.append(rret)
            return min(cands)+1
            
        if root == None:    return 0
        return helper(root)
        
