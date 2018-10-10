class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        for i in range(9): # here, i doesn't represent index for row, but index for (row, column, grid)
            hash_row = {}
            hash_col = {}
            hash_grid = {}
            print("i=", i)

            for j in range(9): # here, j doesn't represent index for column either
                print("j=", j)
                # check the repetition for row
                if board[i][j] != ".":
                    if hash_row.has_key(board[i][j]): return False
                    else: hash_row.setdefault(board[i][j])

                # check the repetition for column
                if board[j][i] != ".":
                    if hash_col.has_key(board[j][i]): return False
                    else: hash_col.setdefault(board[j][i])

                start_row = (i // 3) * 3
                start_col = (i % 3) * 3
                if board[start_row + j % 3][start_col + j % 3] != ".":
                    if hash_grid.has_key(board[start_row + j // 3][start_col + j % 3]): return False
                    else: hash_grid.setdefault(board[start_row + j % 3][start_col + j % 3])

        return True




test = Solution()

x = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

print(test.isValidSudoku(x))