class Solution:
    # @param A, a list of integers
    # @param target, an integer to be inserted
    # @return integer
    def searchInsert(self, A, target):
        start = 0
        end = len(A)-1
        while start <= end:
            mid = (start+end)/2
            if A[mid] == target:
                return mid
            
            elif A[mid] < target:
                start = mid+1
            
            else:
                end = mid-1
    
        '''
            0 1 ... n
        e   s       e   s
            0 1 2 3 ... n
                e s
        '''
        if start < len(A):
            if end >= 0:
                if target < A[end]: return end
                if A[end] < target < A[start]: return start
                if target > A[start]:   return start+1
            else:
                if target < A[start]: return start
                if target > A[start]:   return start+1
        else:
            if target < A[end]: return end
            if target > A[end]:   return end+1

                
        
