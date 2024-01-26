# Constraints:
# 1 <= tokens.length <= 104
# tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].

class Solution:
    # submitted on leetcode with 115ms runtime
    def evalRPN(self, tokens: list[str]) -> int:
        stack_t = []
        for char in tokens:
            if char in ["+", "-", '*', '/']:
                second = stack_t.pop()
                first = stack_t.pop()
                # 6//-132 get -1, but expected 0
                # char = '//' if char == '/' else char
                # idea is from https://program-think.blogspot.com/2009/08/why-choose-python-2-dynamic.html
                result = eval("%s %s %s" % (first, char, second))
                stack_t.append(str(int(result)))
                continue
            stack_t.append(char)

        if len(stack_t) == 1:
            return int(stack_t.pop())
        else:
            return None

    # submitted on leetcode with 64ms runtime
    def evalRPN2(self, tokens: list[str]) -> int:
        stack_t = []
        for char in tokens:
            if char in {"+", "-", '*', '/'}:
                second = stack_t.pop()
                first = stack_t.pop()
                if char == "+":
                    result = first + second
                elif char == "-":
                    result = first - second
                elif char == "*":
                    result = first * second
                else:
                    result = first / second
                stack_t.append(int(result))
                continue
            stack_t.append(int(char))

        if len(stack_t) == 1:
            return stack_t.pop()
        else:
            return None


if __name__ == '__main__':
    sol = Solution()
    print(sol.evalRPN2(tokens=["2", "1", "+", "3", "*"]))
    print(sol.evalRPN2(tokens=["4", "13", "5", "/", "+"]))
    print(sol.evalRPN2(tokens=["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))

# topic is from https://leetcode.com/problems/evaluate-reverse-polish-notation/submissions/1157047758/?envType=study-plan-v2&envId=top-interview-150
# output
# 9
# 6
# 22