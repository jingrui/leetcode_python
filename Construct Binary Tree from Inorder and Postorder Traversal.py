# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param inorder, a list of integers
    # @param postorder, a list of integers
    # @return a tree node
    def buildTree(self, inorder, postorder):
        # print 'inorder = ',inorder
        # print 'postorder = ',postorder
        if len(inorder) == 0:
           return None

        if len(inorder) == 1:
            return TreeNode(inorder[0])


        root = postorder[-1]
        indx = inorder.index(root)
        # print 'root =',root
        # print 'root indx = ',indx

        rightin = inorder[indx+1:]

        if indx-1 > 0: # left is not empty
            leftin = inorder[:indx] # should not be negative
            maxi = max([postorder.index(ele) for ele in leftin])
            leftpo = postorder[:maxi + 1]
            rightpo = postorder[maxi + 1 : -1]
        else:
            leftin = []
            leftpo = []
            rightpo = postorder[: -1]
        
        
        root = TreeNode(root)
        root.left = self.buildTree(leftin, leftpo)
        root.right = self.buildTree(rightin, rightpo)
        return root
