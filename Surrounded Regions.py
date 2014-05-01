class Solution:
    # @param board, a 9x9 2D array
    # Capture all regions by modifying the input board in-place.
    # Do not return any value.
    def solve(self, board):
        group = set()
        groupId = 1
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "X":
                    continue;
                else:
                    # check if at edge
                    if row == 0 or col == 0 or row == len(board)-1 or col == len(board[row])-1:
                        # only need group ID

                        board[row][col] = ['O',float('inf')]
                        # up
                        if row > 0 and type(board[row-1][col])== list:
                            prevgid = board[row][col][1]
                            gid = board[row-1][col][1]
                            board[row][col] = ['O',min(prevgid,gid)]

                        if col > 0 and type(board[row][col-1])== list:
                            prevgid = board[row][col][1]
                            gid = board[row][col-1][1]
                            board[row][col] = ['O',min(prevgid,gid)]
                        group.add(board[row][col][1])
                        
                    else:
                        board[row][col] = ['w',float('inf')]
                        # print row,col
                        # check up
                        if row > 0 and type(board[row-1][col])== list:
                            board[row][col] = board[row-1][col]
                        
                        # for r in board:
                        #     print r
                        # print '1===='
                        # check left
                        if col > 0 and type(board[row][col-1])== list:
                            # print 'board[1][1] = ',board[1][1]
                            if board[row][col-1][0] == 'O':
                                # print row,col
                                board[row][col][0] = 'O'
                                
                                # print 'board[1][1] = ',board[1][1]

                                
                            # for r in board:
                            #     print r
                            # print '2====='

                            prevgid = board[row][col][1]
                            gid = board[row][col-1][1]
                            board[row][col][1] = min(prevgid,gid)
                            # print row,col,board[row][col][1]
                            if board[row][col][0] == 'O':
                                group.add(board[row][col][1])
                            # print group

                        # for r in board:
                        #     print r
                        # print


                    # update groupId
                    if board[row][col][1] == float('inf'):
                        board[row][col][1] = groupId
                        groupId += 1
                    
                    # print "board[",row,"][",col,"]=",board[row][col]

                # for r in board:
                #     print r
                # print

        for row in board:
            print row
        print

        # backtracking
        for row in range(len(board)-1,-1,-1):
            for col in range(len(board[row])-1,-1,-1):
                if board[row][col] == "X":
                    continue;
                else:
                    print row,col
                    if board[row][col][0] == 'O':
                        board[row][col] = 'O'
                    elif board[row][col][1] in group:
                        board[row][col] = 'O'
                    # check right and bottom
                    elif row+1 < len(board[row]) and board[row+1][col] == 'O':
                        board[row][col] = 'O'
                    elif col+1 < len(board) and board[row][col+1] == 'O':
                        board[row][col] = 'O'
                    elif row-1 >= 0 and type(board[row-1][col]) == list and board[row-1][col][1] in group:
                        board[row][col] = 'O'
                    elif col-1 >= 0 and type(board[row][col-1]) == list and board[row][col-1][1] in group:
                        board[row][col] = 'O'
                    else:
                        board[row][col] = 'X'

        # print
        # for row in board:
        #     print row


def printboard(board):
    for row in board:
        print row
    print

board = ["XXXXOX","OXXOOX","XOXOOO","XOOOXO","OOXXOX","XOXOXX"]
for i,row in enumerate(board):
    board[i] = list(row)

printboard(board)
a = Solution()
a.solve(board)

printboard(board)                 

# print "outout"
# board = ["OOOOXX","OOOOOO","OXOXOO","OXOOXO","OXOXXO","OXOOOO"]
# printboard(board)

print "expected"
board = ["XXXXOX","OXXOOX","XOXOOO","XOOOXO","OOXXXX","XOXOXX"]

printboard(board)


