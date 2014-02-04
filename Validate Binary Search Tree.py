# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isValidBST(self, root):
        
        def check(node,up,low):
            if node == None:
                return True
            if up> node.val> low:
                return check(node.left,node.val,low) and check(node.right,up,node.val)
            else:
                return False
        return check(root,float('inf'),float('-inf'))
        
