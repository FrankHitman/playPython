# Constraints:
# 1 <= s.length <= 3 * 105
# s consists of digits, '+', '-', '(', ')', and ' '.
# s represents a valid expression.
# '+' is not used as a unary operation (i.e., "+1" and "+(2 + 3)" is invalid).
# '-' could be used as a unary operation (i.e., "-1" and "-(2 + 3)" is valid).
# There will be no two consecutive operators in the input.
# Every number and running calculation will fit in a signed 32-bit integer.

class Solution:
    # solution is from https://walkccc.me/LeetCode/problems/0224/#__tabbed_1_3
    def calculate(self, s: str) -> int:
        ans = 0
        num = 0
        sign = 1
        stack = [sign]  # stack[-1]: the current environment's sign

        for c in s:
            if c.isdigit():
                num = num * 10 + (ord(c) - ord('0'))
            elif c == '(':
                stack.append(sign)
            elif c == ')':
                stack.pop()
            elif c == '+' or c == '-':
                ans += sign * num
                sign = (1 if c == '+' else -1) * stack[-1]
                num = 0

        return ans + sign * num

    # https://www.geeksforgeeks.org/evaluation-of-postfix-expression/
    # convert the expression to reverse polish notation(related #150)
    def calculate3(self, s: str) -> int:
        stack_s = []
        stack_operat = []
        i = 0
        while i < len(s):
            char = s[i]
            if char == ' ':
                pass
            if char not in {'(', '+', '-', ')'}:
                num = char
                while i < len(s) - 1 and s[i + 1] not in {'(', ')', '+', '-', ' '}:
                    num += s[i + 1]  # connect character
                    i += 1
                stack_s.append(int(num))
            if char in {'+', '-'}:
                stack_operat.append(char)
            i += 1

    # 2-1+2  2 1 - 2 +
    # 3-(4+5) 3 4 5 + -

    # not valid if 2-1 + 2=-1
    def calculate2(self, s: str) -> int:
        stack_s = []
        i = 0
        while i < len(s):
            char = s[i]
            if char == ' ':
                pass
            elif char in {'(', '+', '-'}:
                stack_s.append(char)
            elif char == ')':
                while True:
                    second = stack_s.pop()
                    operat = stack_s.pop()
                    first = stack_s.pop()
                    if first == "(":
                        first = 0
                        sum_p = self.cal(first, second, operat)
                        stack_s.append(sum_p)
                        break
                    elif stack_s[-1] == '(':
                        sum_p = self.cal(first, second, operat)
                        stack_s.pop()
                        stack_s.append(sum_p)
                        break
                    else:
                        sum_p = self.cal(first, second, operat)
                        stack_s.append(sum_p)
            else:
                num = char
                while i < len(s) - 1 and s[i + 1] not in {'(', ')', '+', '-', ' '}:
                    num += s[i + 1]  # connect character
                    i += 1
                stack_s.append(int(num))
            i += 1
        # ['-','(',3,'+','(', '4', '+', '5', ')', ')']
        # "1-(     -2)"
        if len(stack_s) > 1:
            while True:
                # backward calculate will cause 2-1 + 2=-1
                second = stack_s.pop()
                operat = stack_s.pop()
                if len(stack_s) > 0:
                    first = stack_s.pop()
                    sum_p = self.cal(first, second, operat)
                    if len(stack_s) > 0:
                        stack_s.append(sum_p)
                    else:
                        return sum_p
                else:
                    first = 0
                    return self.cal(first, second, operat)
        elif len(stack_s) == 1:
            return stack_s[0]

    def cal(self, first, second, operat):
        if operat == '-':
            return first - second
        elif operat == '+':
            return first + second

    # not valid if s="- (3 + (4 + 5))"
    def calculate1(self, s: str) -> int:
        # remove parentheses
        new_s = ''
        for char in s:
            if char in {'(', ')', ' '}:
                continue
            else:
                new_s += char
        i = 0
        sum_s = 0
        stack_s = []
        while i < len(new_s):
            if new_s[i] == '-':
                num = ''
                while i < len(new_s) - 1 and new_s[i + 1] not in {'+', '-'}:
                    num += new_s[i + 1]  # connect character
                    i += 1
                # handle s="1-(     -2)"
                if len(num) == 0:
                    stack_s.append('-')
                else:
                    stack_s.append(-int(num))
                i += 1
                continue

            elif new_s[i] == '+':
                num = ''
                while i < len(new_s) - 1 and new_s[i + 1] not in {'+', '-'}:
                    num += new_s[i + 1]  # connect character
                    i += 1
                stack_s.append(int(num))
                i += 1
                continue
            else:
                num = new_s[i]
                while i < len(new_s) - 1 and new_s[i + 1] not in {'+', '-'}:
                    num += new_s[i + 1]  # connect character
                    i += 1
                stack_s.append(int(num))
                i += 1
                continue
        j = 0
        while j < len(stack_s):
            if stack_s[j] != '-':
                sum_s += stack_s[j]
            else:
                j += 1
                sum_s -= stack_s[j]
            j += 1
        return sum_s


# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23
if __name__ == '__main__':
    sol = Solution()
    print(sol.calculate(s="1 + 1"))
    print(sol.calculate(s=" 2-1 + 2 "))
    print(sol.calculate(s="(1+(4+5+2)-3)+(6+8)"))
    print(sol.calculate(s="(1+(43+590+2)-398)+(6+8)"))
    print(sol.calculate(s="1-(     -2)"))
    print(sol.calculate(s="- (3 + (4 + 5))"))

# topic is from https://leetcode.com/problems/basic-calculator/?envType=study-plan-v2&envId=top-interview-150
# output
# 2
# 3
# 23
# 252
# 3
# -12
