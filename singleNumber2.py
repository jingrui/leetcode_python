class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        ones = A[0]
        twos = 0
        for ele in A[1:]:
            twos |= ones&ele
            ones ^= ele
            three = ones&twos
            ones &= ~three
            twos &= ~three
        return ones
            
            
