# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param preorder, a list of integers
    # @param inorder, a list of integers
    # @return a tree node
    def buildTree(self, preorder, inorder):
        if len(inorder) == 0:
            return None
        
        value = preorder[0]
        # print "node = "+str(value)
        del preorder[0]
        
        node = TreeNode(value)
        indxInInorder = inorder.index(value)
        leftin = inorder[:indxInInorder]
        rightin = inorder[indxInInorder+1:]
        # print 'leftin=',leftin
        # print 'rightin=',rightin

        # to find leftpre
       
        if len(leftin) == 0:
            leftpre = []
            rightpre = preorder[:]
        else:
            maxi = 0
            for ele in leftin:
                maxi = max(preorder.index(ele), maxi)
            leftpre = preorder[:maxi+1]
            rightpre = preorder[maxi+1:]

        # print 'leftpre=',leftpre
        # print 'rightpre=',rightpre
        
        
        node.left = self.buildTree(leftpre, leftin)
        node.right = self.buildTree(rightpre, rightin)
        return node
        
        
