# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        def helper(node):
            if node == None:
                return None
                
            leftnode = helper(node.left)
            if leftnode != None:
                if node.right!=None:
                    leftnode.left = node.right
                    return helper(node.right)
                else:
                    return leftnode
            else:
                if node.right!= None:
                    node.left = node.right
                    node.right = None
                    return helper(node.left)
                else:
                    return node

            
        helper(root)
        return root
        
