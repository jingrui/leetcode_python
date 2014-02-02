# O(n^2)
class Solution:
    # @return a list of lists of length 3, [[val1,val2,val3]]
    def threeSum(self, num):
        ret = set()
        paird = {}
        count = {}
        for ele in num:
            if count.has_key(ele):
                count[ele] += 1
            else:
                count[ele] = 1
        
        for indx1,ele1 in enumerate(num):
            for indx2 in range(indx1+1,len(num)):
                paird[tuple(sorted((ele1,num[indx2])))] = ele1+num[indx2]
                
        inv = {}
        for key,value in paird.items():
            if inv.has_key(value):
                inv[value].append(key)
            else:
                inv[value] = [key]

        for k in num:
            if inv.has_key(-k):
                for key in inv[-k]:
                    if list(key).count(k) < count[k]: 
                        ele = tuple(sorted([key[0],key[1],k]))
                        if ele not in ret:
                            ret.add(ele)
        ret = map(list,ret)
        return ret

i = [-1,0,1,2,-1,-4,0,0]
# i = [0,-6,0,-14,2,0,-9,5,-9,-8,-7,12,-4,14,-6,6,0,5,-2,6,-7,1,10,-10,-5,3,-2,-3,-13,-6,1,-6,3,9,-5,12,-6,-7,2,0,1,11,-11,4,2,-2,-5,-13,11,0,9,11,-13,-4,-13,-11,14,-8,1,8,1,9,-13,-11,3,-11,9,12,-2,-4,-11,6,14,-7,-5,1,-1,-3,-4,-5,12,12,13,6,-7,-15,10,14,14,-12,8,0,13,2,-3,1,-1,-9,-9,12,-6,-5,-5,-6,4,5,2,10,-13,13,12,6]
s = Solution()
print s.threeSum(i)
