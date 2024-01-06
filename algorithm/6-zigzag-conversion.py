class Solution:
    def convert(self, s: str, numRows: int) -> str:
        index = 0
        row = 0
        flag = 0
        zigzag = ""
        if numRows == 1:
            return s
        while row < numRows:
            while index < len(s):
                zigzag += s[index]
                if flag == 0:
                    step = (numRows - 1 - row) * 2
                    flag = 1
                else:
                    step = row * 2
                    flag = 0
                if step == 0:
                    step = (numRows - 1) * 2
                index += step

            row += 1
            index = row
            # reset flag is very important
            flag = 0

        return zigzag

    # solution from other people on the leetcode
    # this solution fit the letter into the corresponding row in one round
    def convert2(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s

        lst_rows = [''] * numRows
        row_idx = 0
        going_up = False

        for i in range(len(s)):
            lst_rows[row_idx] += s[i]

            if row_idx + 1 == numRows:
                going_up = True
            elif row_idx == 0:
                going_up = False

            if going_up:
                row_idx -= 1
            else:
                row_idx += 1

        return ''.join(lst_rows)


if __name__ == '__main__':
    sol = Solution()
    print(sol.convert(s="PAYPALISHIRING", numRows=3))
    print(sol.convert(s="PAYPALISHIRING", numRows=4))
    print(sol.convert(s="A", numRows=1))
    print(sol.convert2(s="PAYPALISHIRING", numRows=4))

# topic is from https://leetcode.com/problems/zigzag-conversion/submissions/1138469488/?envType=study-plan-v2&envId=top-interview-150
# output
# PAHNAPLSIIGYIR
# PINALSIGYAHRPI
# A
# PINALSIGYAHRPI