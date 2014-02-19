#Pascal'sTriangle
class Solution:
    # @return a list of lists of integers
    def generate(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        ret = [[1],[1,1]]
        for i in range(numRows-2):
            above = ret[-1]
            currow = [above[i-1]+above[i] for i in range(1,len(above))]
            currow.insert(0,1)
            currow.append(1)
            ret.append(currow)
        return ret
