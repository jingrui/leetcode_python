# Since mid = (start+end)/2, 3,4 go to 3, 
# thus alwasys include mid in the lower half would be good
# lower = [start:mid], it would finally get to one start=end
# same thing for upper = [mid+1:end]

class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        return [self.helper(A, target-0.1, 0, len(A)-1), self.helper(A, target+0.1, 0, len(A)-1)]
        
    def helper(self, A, target, start, end):
        if start == end:
            if abs(A[start] - target) < 0.1001:
                return start
            else: 
                if A[start] < target:
                    if start+1 < len(A) and abs(A[start+1] - target) < 0.1001:
                        return start+1

                if A[start] > target  and abs(A[start-1] - target) < 0.1001:
                    if start-1 >= 0:
                        return start-1

                return - 1
        
        mid = (start+end)/2
        if A[mid] < target:
            return self.helper(A, target, mid+1, end)
        else:
            return self.helper(A, target, start, mid)

a = Solution()
print a.searchRange([1,3],1)