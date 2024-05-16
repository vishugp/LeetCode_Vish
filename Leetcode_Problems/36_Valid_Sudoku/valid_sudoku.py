class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(len(board)):
            #row
            l = [x for x in board[i] if x!="."]
            if len(set(l))!=len(l):
                # print(i)
                return False, l, i, 'r'
            
            #column
            l = [board[j][i] for j in range(len(board))]
            l = [k for k in l if k!="."]
            if len(set(l))!=len(l):
                # print(l)
                return False, l, i, 'c'
            
        for ulimit in [[0,1,2],[3,4,5],[6,7,8]]:
            for ulimit2 in [[0,1,2],[3,4,5],[6,7,8]]:
                l = [board[a1][a2] for a1 in ulimit for a2 in ulimit2]
                l = [k for k in l if k!="."]
                if len(set(l))!=len(l):
                    # print(l)
                    return False, l, (ulimit, ulimit2), 'b'
                
        return True
            
            
a = Solution()
board = [
    [".",".","5",".",".",".",".",".","6"],
    [".",".",".",".","1","4",".",".","."],
    [".",".",".",".",".",".",".",".","."],
    [".",".",".",".",".","9","2",".","."],
    ["5",".",".",".",".","2",".",".","."],
    [".",".",".",".",".",".",".","3","."],
    [".",".",".","5","4",".",".",".","."],
    ["3",".",".",".",".",".","4","2","."],
    [".",".",".","2","7",".","6",".","."]]


print(a.isValidSudoku(board))