#UniqueBinarySearchTrees
class Solution:
    # @return an integer
    def numTrees(self, n):
    	if n == 0: return 1
    	ways =[0 for i in range(n+1)]
        ways[0] = 1
        ways[1] = 1

        for i in range(2,n+1):
        	for root in range(1,i+1):
        		left = root-1
        		right = i-root
        		ways[i] += ways[left]*ways[right]
        return ways[-1]
