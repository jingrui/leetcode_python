class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) <= 1: return 0
        canReach = 0
        lastCanReach = 0
        indx = 0
        step = 0
        while indx <= canReach < len(A) -1 :
            if indx + A[indx] > canReach:
                canReach = indx + A[indx]
                if indx >= lastCanReach:
                    step += 1
                    lastCanReach = canReach
            indx += 1
        return step
        
a = Solution()
print a.jump([2,3,0,1,4])         
