class Solution:
    # @param A  a list of integers
    # @param m  an integer, length of A
    # @param B  a list of integers
    # @param n  an integer, length of B
    # @return nothing
    def merge(self, A, m, B, n):
        pa = m-1
        pb = n-1
        indx = len(A)-1
        while indx >= 0:
            if pa < 0:
                A[indx] = B[pb]
                pb-=1
            elif pb < 0:
                A[indx] = A[pa]
                pa-=1
            elif A[pa]>B[pb]:
                A[indx]=A[pa]
                pa-=1
            else:
                A[indx]=B[pb]
                pb-=1
            indx-=1
        
        
