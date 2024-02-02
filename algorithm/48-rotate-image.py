# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

class Solution:
    # idea is inspired by https://leetcode.com/problems/rotate-image/description/comments/1574669
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row_len = col_len = len(matrix)
        for r in range(row_len):
            for c in range(r, col_len):
                temp = matrix[r][c]
                matrix[r][c] = matrix[c][r]
                matrix[c][r] = temp

        for r in range(row_len):
            left = 0
            right = col_len - 1
            while left < right:
                matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                left += 1
                right -= 1
        print(matrix)


if __name__ == '__main__':
    sol = Solution()
    sol.rotate(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    sol.rotate(matrix=[[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])

# check picture file: 48-rotate-image.png for the mindset
# topic is from https://leetcode.com/problems/rotate-image/submissions/1155325726/?envType=study-plan-v2&envId=top-interview-150
# output
# [[7, 4, 1], [8, 5, 2], [9, 6, 3]]
# [[15, 13, 2, 5], [14, 3, 4, 1], [12, 6, 8, 9], [16, 7, 10, 11]]
