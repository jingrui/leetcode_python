class Solution:
    # @param matrix, a list of lists of integers
    # @return a list of lists of integers
    def rotate(self, matrix):
        n = len(matrix)-1 
        for row in range((len(matrix)+1)/2):
            for col in range((len(matrix)+0)/2):
                origin = matrix[row][col]
                
                matrix[row][col]   = matrix[n - col][row]
                matrix[n - col][row] = matrix[n - row][n - col]
                matrix[n - row][n - col] = matrix[col][n - row]
                matrix[col][n - row] = origin
        return matrix
                
        