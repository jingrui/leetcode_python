class Solution:
    # @return a list of lists of integers
    def combine(self, n, k):
        ret = []
        self.helper(n,k,1,[], ret)
        return ret
        
    def helper(self, n, k, start, cur, ret):

        if k == 0:
            ret.append(cur)
            return 

        if start > n:
            return

        curcopy = cur[:]
        self.helper(n, k, start+1, curcopy, ret)

        cur.append(start)
        self.helper(n, k-1, start+1, cur, ret)


a = Solution()
print a.combine(4,2)