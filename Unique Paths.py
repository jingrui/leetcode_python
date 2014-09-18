class Solution:
    # @return an integer
    def uniquePaths(self, m, n):
        arr = [[1 for j in range(n)] for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    arr[i][j] = arr[i][j-1]
                elif j == 0:
                    arr[i][j] = arr[i-1][j]
                else:
                    arr[i][j] = arr[i-1][j] + arr[i][j-1]
        return arr[-1][-1]
                
                