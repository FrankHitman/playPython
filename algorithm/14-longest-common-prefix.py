# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
#
#
# Constraints:
#
# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] consists of only lowercase English letters.

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        common_s = ""
        index = 0
        try:
            while index < len(strs[0]):
                common_l = strs[0][index]
                for i in range(1, len(strs)):
                    if common_l != strs[i][index]:
                        return common_s
                common_s += common_l
                index += 1

        except Exception as e:
            print(e)
            return common_s

        return common_s

    # other people's solution from leetcode with 30ms runtime
    def longestCommonPrefix2(self, strs: list[str]) -> str:
        if (len(strs) < 1):
            return ""
        v = sorted(strs)
        first = v[0]
        last = v[len(v) - 1]
        prefix = ''
        for i in range(min(len(first), len(last))):
            if (first[i] == last[i]):
                prefix += first[i]
            else:
                break
        return prefix


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestCommonPrefix(["flower", "flow", "flight"]))
    print(sol.longestCommonPrefix(["dog", "racecar", "car"]))
    print(sol.longestCommonPrefix([]))
    print(sol.longestCommonPrefix(["flower", "flow", "flight", "f"]))

# topic is from https://leetcode.com/problems/longest-common-prefix/submissions/1135679004/?envType=study-plan-v2&envId=top-interview-150
# output of 40ms runtime
# fl
#
# list index out of range
#
# string index out of range
# f
