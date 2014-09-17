class Solution:
    # @param num, a list of integer
    # @return a list of lists of integer
    def subsetsWithDup(self, S):
        S = sorted(S)
        countMap = {}
        numbers = []
        for number in S:
            if countMap.has_key(number):
                continue
            else:
                numbers.append(number)
                countMap[number] = S.count(number)
        
        ret = []
        # print numbers, countMap
        self.helper(0, numbers, countMap, [], ret)
        return ret
    
    def helper(self, i, numbers, countMap, curlist, ret):
        
        if i == len(numbers):
            ret.append(curlist)
            return
        
        number = numbers[i]
        for count in range(countMap[number]+1):
            curlistcopy = curlist[:] + count * [number]
            # print count, number, curlist, curlistcopy
            self.helper(i+1, numbers, countMap, curlistcopy, ret)
                
                
a = Solution()
print a.subsetsWithDup([7,8])