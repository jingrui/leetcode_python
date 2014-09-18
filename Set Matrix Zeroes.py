class Solution:
    # @param matrix, a list of lists of integers
    # RETURN NOTHING, MODIFY matrix IN PLACE.
    def setZeroes(self, matrix):
        for row in range(len(matrix)):
            rowNone = False
            for col in range(len(matrix[row])):
                if matrix[row][col] == 0:
                    rowNone = True
                    for row2 in range(len(matrix)):
                        if matrix[row2][col] != 0:
                            matrix[row2][col] = None
            if rowNone:
                matrix[row] = [0]*len(matrix[row])
                
        for row in range(len(matrix)):
             for col in range(len(matrix[row])):
                  if matrix[row][col] == None:
                       matrix[row][col] = 0
                            
                        
        