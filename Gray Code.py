class Solution:
    # @return a list of integers
    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0,1]
        else:
            ret = self.grayCode(n-1)
            diff = pow(2, n - 1)
            return ret + map((lambda x:x+diff), ret[::-1])
            
            
        
a = Solution()
ret a.grayCode(2)
