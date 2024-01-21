# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

# the usage of collections.defaultdict
# s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d = defaultdict(list)
# for k, v in s:
#     d[k].append(v)
#
# sorted(d.items())
# [('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

import collections

# idea if from https://www.youtube.com/watch?v=TjFXEUCMqI8&ab_channel=NeetCode
class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        row = collections.defaultdict(set)
        col = collections.defaultdict(set)
        square = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in row[r] or \
                        board[r][c] in col[c] or \
                        board[r][c] in square[(r // 3, c // 3)]:
                    # instead of board[r][c] in square[r//3][c//3]:
                    # the key to find a representative to represent the 3*3 sub-boxes
                    return False
                row[r].add(board[r][c])
                col[c].add(board[r][c])
                square[(r // 3, c // 3)].add(board[r][c])
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValidSudoku(board=
                            [["5", "3", ".", ".", "7", ".", ".", ".", "."]
                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(sol.isValidSudoku(board=
                            [["8", "3", ".", ".", "7", ".", ".", ".", "."]
                                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]))
    print(sol.isValidSudoku(
        [[".", "8", "7", "6", "5", "4", "3", "2", "1"], ["2", ".", ".", ".", ".", ".", ".", ".", "."],
         ["3", ".", ".", ".", ".", ".", ".", ".", "."], ["4", ".", ".", ".", ".", ".", ".", ".", "."],
         ["5", ".", ".", ".", ".", ".", ".", ".", "."], ["6", ".", ".", ".", ".", ".", ".", ".", "."],
         ["7", ".", ".", ".", ".", ".", ".", ".", "."], ["8", ".", ".", ".", ".", ".", ".", ".", "."],
         ["9", ".", ".", ".", ".", ".", ".", ".", "."]]))

# topic is from https://leetcode.com/problems/valid-sudoku/submissions/1152629816/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# False
# True