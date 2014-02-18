# SearchinRotatedSortedArray 
'''
(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
'''
class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return an integer
    
    def search(self, A, target):
    	def helper(s,e,a,t):
    		if e < s:
    			return -1
    		else:
    			mid = (s+e)/2
    			if a[mid] == t:
    				return mid

    			# lowest at left
    			if a[s] > a[mid]:
    				if a[mid] < t <= a[e]:
    					# go right
    					return helper(mid+1,e,a,t)
    				else:# go left
    					return helper(s,mid-1,a,t)
    			else:# a[mid] > a[s], lowest at right
    				if a[s] <= t < a[mid]:
    					return helper(s,mid-1,a,t)
    				else:
    					return helper(mid+1,e,a,t)

    	return helper(0,len(A)-1,A,target)

        
