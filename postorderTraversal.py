# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of integers
    def postorderTraversal(self, root):
        def helper(node,ret):
            if node!=None:
                helper(node.left,ret)
                helper(node.right,ret)
                ret.append(node.val)
        ret = []
        helper(root,ret)
        return ret
