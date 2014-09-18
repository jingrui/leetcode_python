class Solution:
    # @param A a list of integers
    # @param target an integer
    # @return a boolean
    def search(self, A, target):
        return self.helper(A, target, 0 , len(A)-1)
    
    def helper(self, A, target, s, e):
        if s > e :
            return False
            
        mid = (s + e)/2
        if A[mid] == target:
            return True
        elif A[mid] < A[e]:
            if A[mid] < target <= A[e]:
                return self.helper(A, target, mid+1, e)
            else:
                return self.helper(A, target, s, mid-1)
        elif A[s] < A[mid]:
            if A[s] <= target < A[mid]:
                return self.helper(A, target, s, mid-1)
            else:
                return self.helper(A, target, mid+1, e)
        else:
        	return self.helper(A, target, s, mid-1) or self.helper(A, target, mid+1, e)
            
        
a = Solution()
print a.search([1,1,3,1], 3)