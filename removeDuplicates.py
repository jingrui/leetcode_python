class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if len(A) == 0: return 0
        quick = 1
        slow = 0
        while quick < len(A):
            if A[quick] != A[slow]:
                slow +=1
                A[slow] = A[quick]
                
            quick+=1
        return slow+1
        
