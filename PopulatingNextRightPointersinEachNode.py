# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree node
    # @return nothing
    def connect(self, root):
        if root == None:    return
        q = [root]
        q2 = []
        while len(q) != 0:
            while len(q)!= 0:
                top = q[0]
                del q[0]
                if len(q) > 0:
                    top.next = q[0]
                if top.left!=None:
                    q2.append(top.left)
                if top.right!=None:
                    q2.append(top.right)
            q = q2
            q2 = []
            
                    
            
        
