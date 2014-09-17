class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        board = []
        ret = []
        for col in range(n): 
            board.append(col)
            self.helper(n, board, ret)
            board.pop()
        
        for indx, conf in enumerate(ret):
            rows = []
            for col in conf:
                rows.append("." * col  + "Q" + "." * (n-col-1))
            ret[indx] = rows
        return ret
            
                    
    
    def helper(self, n, board, ret):

        thisR = len(board)
        if thisR == n:
            ret.append(board[:])
            return
        
        for col in range(n):
            poss = True
            for row in range(len(board)):
                if abs(thisR-row) == abs(board[row] - col) or col == board[row]:
                    poss = False
                    break
            if poss:
                board.append(col)
                self.helper(n, board, ret)
                board.pop()
        
        
        
        
a = Solution()
ret = a.solveNQueens(1)
for conf in ret:
    for row in conf:
        print row
    print