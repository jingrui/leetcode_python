# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # @param root, a tree node
    # @return a boolean
    # always return the deepest depth
    def isBalanced(self, root):
        def helper(node):
            if node == None:
                return 0
            
            l = helper(node.left)
            r = helper(node.right)
            if l < 0 or r < 0 or abs(l-r)>1:
                return -1
            else:
                return max([r,l])+1
        return helper(root)>=0
        
