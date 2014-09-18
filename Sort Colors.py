class Solution:
    # @param A a list of integers
    # @return nothing, sort in place
    def sortColors(self, A):
        left = 0
        right = len(A)-1
        cur = 0
        while left <= cur <= right:
            if A[cur] == 1:
                cur += 1
            elif A[cur] == 0:
                A[left], A[cur] = A[cur],A[left]
                left += 1
                cur += 1
            else:
                A[cur], A[right] = A[right], A[cur]
                right -= 1
        return A
        