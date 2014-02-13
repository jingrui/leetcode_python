class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        cur = 0
        elep = 0
        
        while cur < len(A):
            while elep < len(A) and A[elep] != elem:
                elep +=1
            if elep == len(A): break
            
            if cur == 0:
                cur = elep
            # elep point to elem
            # find the next not elem 
            
            while cur < len(A) and A[cur]==elem:
                cur+=1
            if cur >= len(A):   break
        
            A[cur],A[elep] = A[elep],A[cur]
            elep+=1
            cur +=1
        return elep
            
        
