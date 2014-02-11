# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return an integer
    def sumNumbers(self, root):
    	def helper(node,cur,ret):
    		cur = [node.val]+cur
    		# print node.val,cur,ret
    		if node.left == None and node.right == None:
    			# print 'leaf'
    			ret.append(cur)
    			return

    		if node.left != None:
    			# print 'left'
    			helper(node.left,cur[:],ret)
    		if node.right != None:
    			# print 'right'
    			helper(node.right,cur[:],ret)

        if root == None:    return 0
    	ret = []
    	helper(root,[],ret)
    	number = []
    	indx = 0
    	# print ret
    	carry = 0
    	while indx < max(map(len,ret)):
    		n = sum([ele[indx] for ele in ret if indx < len(ele)])+carry
    		carry = n/10
    		n = n%10
    		number.append(n)
    		indx +=1
    	if carry!=0:
    		number.append(carry%10)
    		carry/=10
    	# print number
    	number.reverse()
    	number = ''.join(map(str,number))
    	return int(number)

r = TreeNode(5)
r.left = TreeNode(6)
r.right = TreeNode(7)
a = Solution()
print a.sumNumbers(r)


        
