#Triangle
class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):
        if len(triangle) == 0: return 0
        for indxr,row in enumerate(triangle[:len(triangle)-1]):
            row.insert(0,float('inf'))
            row.append(float('inf'))
            print row
            for indxc,col in enumerate(row[1:]):
                if row[indxc+1] < row[indxc]:
                    triangle[indxr+1][indxc] += row[indxc+1]
                else:
                    triangle[indxr+1][indxc] += row[indxc]
        return min(triangle[-1])

    def minimumTotal2(self, triangle):
        if len(triangle) == 0: return 0
        numb = float('inf')
        total = [numb]+triangle[0]+[numb]
        # print total
        for row in triangle[1:]:
            newtotal = [min([total[indx],total[indx+1]])+row[indx] for indx,ele in enumerate(row)]
            total = [numb]+newtotal+[numb]
            # print total
        del total[0]
        del total[-1]
        return min(total)
                
l = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
a = Solution()
print a.minimumTotal(l)
