# Constraints:
# 1 <= s.length <= 104
# s consists of parentheses only '()[]{}'.

class Solution:
    def isValid(self, s: str) -> bool:
        stack_c = []
        try:
            for character in s:
                if character in ["{", "(", "["]:
                    stack_c.append(character)
                elif character == "}":
                    pre_c = stack_c.pop()
                    if pre_c != "{":
                        return False
                elif character == ")":
                    pre_c = stack_c.pop()
                    if pre_c != "(":
                        return False
                elif character == "]":
                    pre_c = stack_c.pop()
                    if pre_c != "[":
                        return False
            if len(stack_c) > 0:
                return False
            return True

        except Exception as e:
            print(e)
            return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isValid(s="()"))
    print(sol.isValid(s="()[]{}"))
    print(sol.isValid(s='{[[]](}'))
    print(sol.isValid(s='{[[]]()}'))
    print(sol.isValid(s="(]"))
    print(sol.isValid(s="("))

# topic is from https://leetcode.com/problems/valid-parentheses/submissions/1155366324/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# True
# False
# True
# False
# False