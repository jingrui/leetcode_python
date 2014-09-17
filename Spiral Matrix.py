class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of integers
    def spiralOrder(self, matrix):
        if len(matrix) == 0:
            return []
            
        ret = []
        rows = len(matrix)
        cols = len(matrix[0])
        startx = 0
        starty = 0
        while len(matrix) > 0 and len(matrix[0]):
            for ele in matrix[0]:
                ret.append(ele)
            del matrix[0]
            
            for row in range(len(matrix)):
                if len(matrix[row]) > 0:
                    ret.append(matrix[row][-1])
                    del matrix[row][-1]
                
            if len(matrix) > 0:
                print matrix[-1], matrix
                while len(matrix[-1]) > 0:
                    ret.append(matrix[-1].pop())
                del matrix[-1]
            
            for row in range(len(matrix)-1,-1,-1):
                if len(matrix[row]) > 0:
                    ret.append(matrix[row][0])
                    del matrix[row][0]
                
        return ret
            
            
                
a = Solution()
print a.spiralOrder([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20],[21,22,23,24,25]])
# [[1,2,3,4]
# ,[5,6,7,8]
# ,[9,10,11,12]
# ,[13,14,15,16]]

