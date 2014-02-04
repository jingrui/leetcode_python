class Solution:
    # @param S, a list of integer
    # @return a list of lists of integer
    def subsets(self, S):
        ret = []
        def add(cur,indx):
            if indx == len(S):
                ret.append(cur)
            else:
                add(cur+[S[indx]],indx+1)
                add(cur,indx+1)
        add([],0)
        for ele in ret:
            ele.sort()
        return sorted(ret)
            
