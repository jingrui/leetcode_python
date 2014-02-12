# BinaryTreeMaximumPathSum 
# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def maxPathSum(self, root):
    	'''
    	find the one from left to cur,right to cur sum them up and 
    	compare with largest from left,largest from right
    	return largest from leave to cur,largest within left to right through cur
        '''
        def helper(node):
        	if node == None:
        		return 0,float('-inf')

        	ll2c,lbest = helper(node.left)
        	rl2c,rbest = helper(node.right)
        	bestleave2leave = max([lbest,rbest,max([0,ll2c])+max([0,rl2c])+node.val,])
        	bestleavetocur = max([ll2c,rl2c,0])+node.val
        	return bestleavetocur,bestleave2leave
        return max(helper(root))
