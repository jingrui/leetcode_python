class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        def helper(cur, num, ret):
            if len(num)==0:
                ret.append(cur)
            else:
                for i in range(len(num)):
                    ncopy = num[:]
                    ccopy = cur+[ncopy[i]]
                    del ncopy[i]
                    helper(ccopy,ncopy,ret)
        ret = []
        helper([],num,ret)
        return ret
                    
            
        
