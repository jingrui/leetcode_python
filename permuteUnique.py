class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    

    def permuteUnique(self, num):
        def deepcopy(d):
            copy = dict()
            for key, val in d.items():
                copy[key] = val
            return copy

        def helper(cur, num, numdic, ret):
            # print 
            if len(num)==0:
                ret.append(cur)
            else:
                for ele in numdic.keys():
                    ndiccopy = deepcopy(numdic)
                    if ndiccopy[ele] == 1:
                        del ndiccopy[ele]
                    else:
                        ndiccopy[ele] -=1

                    indx = num.index(ele)
                    ncopy = num[:]
                    ccopy = cur+[num[indx]]
                    del ncopy[indx]
                    helper(ccopy,ncopy,ndiccopy,ret)
        numdic = dict([(ele,num.count(ele)) for ele in num])
        ret = []
        helper([],num,numdic,ret)
        return ret
