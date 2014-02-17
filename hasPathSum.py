# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a boolean
    def hasPathSum(self, root, sum):
        def helper(node,target):
            if node == None:    return False
            if node.left == None and node.right  == None:
                if target == node.val:
                    return True
                else:
                    return False
            else:
                return helper(node.left,target-node.val) or helper(node.right,target-node.val)
            
        return helper(root,sum)
        
