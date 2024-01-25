# Constraints:
# 1 <= path.length <= 3000
# path consists of English letters, digits, period '.', slash '/' or '_'.
# path is a valid absolute Unix path.

class Solution:
    def simplifyPath(self, path: str) -> str:
        split_p = path.split('/')
        stack_p = []
        try:
            for item in split_p:
                if item == '':
                    continue
                elif item == '.':
                    continue
                elif item == '..':
                    if len(stack_p) >= 1:
                        stack_p.pop()
                else:
                    stack_p.append(item)

        except Exception as e:
            print(e)
        return '/' + '/'.join(stack_p)


if __name__ == '__main__':
    sol = Solution()
    print(sol.simplifyPath(path="/home/"))
    print(sol.simplifyPath(path="/../"))
    print(sol.simplifyPath(path="/home//foo/"))

# topic is from https://leetcode.com/problems/simplify-path/description/?envType=study-plan-v2&envId=top-interview-150
# output
# /home
# /
# /home/foo