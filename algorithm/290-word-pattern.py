# Constraints:
# 1 <= pattern.length <= 300
# pattern contains only lower-case English letters.
# 1 <= s.length <= 3000
# s contains only lowercase English letters and spaces ' '.
# s does not contain any leading or trailing spaces.
# All the words in s are separated by a single space.


class Solution:
    # idea is inspired by 205-isomorphic-strings solution2
    def wordPattern(self, pattern: str, s: str) -> bool:
        pat_map = {}
        s_list = s.split(' ')
        if len(pattern) != len(s_list):
            return False

        for i in range(len(pattern)):
            if pattern[i] in pat_map:
                if pat_map[pattern[i]] != s_list[i]:
                    return False
            else:
                if s_list[i] not in pat_map.values():
                    pat_map[pattern[i]] = s_list[i]
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.wordPattern(pattern="abba", s="dog cat cat dog"))
    print(sol.wordPattern(pattern="abba", s="dog cat cat fish"))
    print(sol.wordPattern(pattern="aaaa", s="dog cat cat dog"))

# topic is from https://leetcode.com/problems/word-pattern/description/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# False
# False