# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return a list of lists of integers
    def levelOrder(self, root):
        if root == None:
            return []
        
        def helper(nodelist,ret):
            if len(nodelist)!=0:
                nextlevel = []
                ret.append(map(lambda x: x.val,nodelist))
                while len(nodelist)!=0:
                    n = nodelist[0]
                    del nodelist[0]
                    if n.left!=None:
                        nextlevel.append(n.left)
                    if n.right!=None:
                        nextlevel.append(n.right)
                helper(nextlevel,ret)
        ret = [] 
        helper([root],ret)
        return ret 
        
