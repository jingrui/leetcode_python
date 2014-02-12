# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def preorderTraversal(self, root):
        def helper(node,ret):
            if node != None:
                ret.append(node.val)
                helper(node.left,ret)
                helper(node.right,ret)
        ret = []
        helper(root,ret)
        return ret
        
