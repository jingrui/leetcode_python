class Solution:
    # @param A a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        
        if len(A) == 0:
            return 0
        
        prev = A[0]
        count = 1
        ret = 1
        indx = 1
        while indx < len(A):
            ele = A[indx]
            if ele == prev:
                count += 1
                if count <= 2:
                    ret += 1
                else:
                    del A[indx]
                    continue
                    
            else:
                prev = ele
                count = 1
                ret += 1
            indx += 1
            
        return ret
        