class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        indx = 0
        while indx < len(A):
            print indx,A
            ele = A[indx]
            if len(A) > ele-1>= 0 and indx!= ele-1 and A[ele-1]!= ele:
                A[ele-1],A[indx] = ele,A[ele-1]
            else:
                indx+=1
                
                
        for indx,ele in enumerate(A):
            if ele!= indx+1:
                return indx+1
        return len(A)+1
        
i = [3,4,-1,1]
i = [1,1]
s = Solution()
print s.firstMissingPositive(i)
