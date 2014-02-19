class Solution:
    # @return a list of integers
    def getRow(self, rowIndex):
        if rowIndex == 0:   return []
        rowFac = reduce(lambda x,y: x*y,range(1,rowIndex+1))
        # print rowFac
        denom = []
        fac = rowFac
        ifac = 1
        for i in range(1,rowIndex/2+1):
            fac /= (rowIndex-i+1)
            ifac *=i
            # print ifac,fac

            denom.append((ifac*fac))
        denom2 = denom[::-1]
        if rowIndex%2 == 0:
            del denom2[0]
        denom.extend(denom2)
        # print denom
        denom = map(lambda ele: rowFac/ele,denom)
        denom.insert(0,1)
        denom.append(1)
        # print denom
        return denom



import sys
a = Solution()
print a.getRow(int(sys.argv[1]))
                
        
        
