# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrderBottom(self, root):
        if root == None:
            return []
            
        res = []
        q1 = [root]
        q2 = []
        while len(q1) > 0:
            curlevel = []
            while len(q1) > 0:
                top = q1[0]
                curlevel.append(top.val)
                del q1[0]
                if top.left != None:
                    q2.append(top.left)
                if top.right != None:
                    q2.append(top.right)
            q1 = q2
            q2 = []
            res.insert(0, curlevel)
        return res
            
        
        
