class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    def combinationSum(self, candidates, target):
        def helper(cand,t,indx,cur,ret):
            if sum(cur) > t or indx >= len(cand):
                return False
            if sum(cur) == t:
                ret.append(cur)
                return True
            # print 'indx = ',indx,',cur=',cur,',ret=',ret
            ret1 = helper(cand,t,indx,cur+[cand[indx]],ret)
            if ret1 != True:
                helper(cand,t,indx+1,cur[:],ret)
                
        candidates.sort()
        ret = []
        helper(candidates,target,0,[],ret)
        return ret
