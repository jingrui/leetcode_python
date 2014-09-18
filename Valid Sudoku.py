class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def isValidSudoku(self, board):
        ret = True

        # rows
        for row in board:
            l = []
            for ele in row:
                if ele != ".":
                    l.append(ele)
            ret = ret and self.validate(l)
        print ret

        # cols
        for col in range(len(board[0])):
            l = []
            for row in board:
                if row[col] != ".":
                    l.append(row[col])
            ret = ret and self.validate(l)
        print ret

        # cells
        for i in range(len(board)):
            row = i/3 * 3
            col = i%3 * 3
            l = []
            for rowN in range(row, row+3):
                for colN in range(col, col+3):
                    if board[rowN][colN] != ".":
                        l.append(board[rowN][colN])
            ret = ret and self.validate(l)
        print ret

            
        return ret
        
    
    def validate(self, l):
        return len(set(l)) == len(l)

l = [".87654321","2........","3........","4........","5........","6........","7........","8........","9........"]
a = Solution()
a.isValidSudoku(l)