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

            for j in range(9): # here, j doesn't represent index for column either
                # check the repetition for row
                if board[i][j] != ".":
                    if (board[i][j] in hash_row): return False
                    else: hash_row.setdefault(board[i][j])

                # check the repetition for column
                if board[j][i] != ".":
                    if (board[j][i] in hash_col): return False
                    else: hash_col.setdefault(board[j][i])

                start_row   = (i // 3) * 3
                start_col = (i % 3) * 3
                if board[start_row + j // 3][start_col + j % 3] != ".":
                    if (board[start_row + j // 3][start_col + j % 3] in hash_grid): return False
                    else: hash_grid.setdefault(board[start_row + j // 3][start_col + j % 3])

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