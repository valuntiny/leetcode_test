'''
You are given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).
'''

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        matrix.reverse()

        i = 0
        while i < len(matrix[1]):
            j = i + 1
            while j < len(matrix[1]):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
                j += 1
            i += 1


x = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]

test = Solution()
test.rotate(x)

print(x)

