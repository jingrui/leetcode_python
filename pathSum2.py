# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @param sum, an integer
    # @return a list of lists of integers
    def pathSum(self, root, sum):
        def helper(node,cur,target,ret):
            if node == None:
                return
            if node.left == None and node.right == None:
                if node.val == target:
                    cur.append(node.val)
                    ret.append(cur)
                    return 
                else:
                    return
            else:
                helper(node.left,cur+[node.val],target-node.val,ret)
                helper(node.right,cur+[node.val],target-node.val,ret)
                
                
        ret = []
        helper(root,[],sum,ret)
        return ret
        
