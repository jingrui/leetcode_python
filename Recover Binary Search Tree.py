# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a tree node
    def recoverTree(self, root):
        helper(root)
        
    def helper(self, prev, node, first, second):
        if node == None:
            return None
            
        if prev == None:
            prev = helper(prev, node.left)
        else:
            helper(prev, node.left)



        # helper(prev, node.left)
        # if prev == None:
        #     prev = node
        # else:
        #     if prev.val > node.val:
        #         if first == None:
        #             first = node
        #         else:
        #             second = node
                    
        
        # prev = helper(node, node.right)
        # if prev == None:
        #     return node
        # else:
        #     return prev
        
        # 