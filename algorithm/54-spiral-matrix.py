# Constraints:
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 10
# -100 <= matrix[i][j] <= 100

class Solution:
    # solution is inspired by https://medium.com/nerd-for-tech/leetcode-spiral-matrix-60d7568b50ca
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        row_start = 0
        row_stop = len(matrix) - 1
        col_start = 0
        col_stop = len(matrix[0]) - 1
        output = []
        output_num = (row_stop + 1) * (col_stop + 1)

        while row_start <= row_stop and col_start <= col_stop:
            pointer = col_start
            while col_start <= pointer <= col_stop and len(output) < output_num:
                output.append(matrix[row_start][pointer])
                pointer += 1
            row_start += 1

            pointer = row_start
            while row_start <= pointer <= row_stop and len(output) < output_num:
                output.append(matrix[pointer][col_stop])
                pointer += 1
            col_stop -= 1

            pointer = col_stop
            while col_start <= pointer <= col_stop and len(output) < output_num:
                output.append(matrix[row_stop][pointer])
                pointer -= 1
            row_stop -= 1

            pointer = row_stop
            while row_start <= pointer <= row_stop and len(output) < output_num:
                output.append(matrix[pointer][col_start])
                pointer -= 1
            col_start += 1

        return output


if __name__ == '__main__':
    sol = Solution()
    print(sol.spiralOrder(matrix=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
    print(sol.spiralOrder(matrix=[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]))

# topic is from https://leetcode.com/problems/spiral-matrix/submissions/1155293970/?envType=study-plan-v2&envId=top-interview-150
# output
# [1, 2, 3, 6, 9, 8, 7, 4, 5]
# [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
