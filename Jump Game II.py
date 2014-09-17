class Solution:
    # @param A, a list of integers
    # @return an integer
    def jump(self, A):
        if len(A) <= 1: return 0
        canReach = 0
        lastCanReach = 0
        indx = 0
        step = 0
        while indx <= canReach <= len(A) - 2 :
            while indx <= lastCanReach <= len(A) -2 :
                if indx + A[indx] > canReach:
                    canReach = indx + A[indx]
                indx += 1

            if canReach > lastCanReach:
                step += 1
                lastCanReach = canReach


        return step
        
a = Solution()
print a.jump([4,2,1,3,2,1,0])         
# 