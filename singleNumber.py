class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ret = A[0]
        for ele in A[1:]:
            ret ^=ele
        return ret
        
