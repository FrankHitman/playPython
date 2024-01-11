# Constraints:
# 0 <= s.length <= 100
# 0 <= t.length <= 104
# s and t consist only of lowercase English letters.

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False
        i = 0
        j = 0
        while j < len(t):
            if s[i] != t[j]:
                j += 1
            else:
                i += 1
                j += 1
            if i >= len(s):
                return True
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.isSubsequence(s="abc", t="ahbgdc"))
    print(sol.isSubsequence(s="axc", t="ahbgdc"))
    print(sol.isSubsequence(s="", t="ahbgdc"))

# topic is from https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# False
# False