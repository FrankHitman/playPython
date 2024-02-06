# Constraints:
# 1 <= s.length, t.length <= 5 * 104
# s and t consist of lowercase English letters.


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False

        st_map = {}
        for i in s:
            st_map[i] = st_map.get(i, 0) + 1
        for i in t:
            if i not in st_map:
                return False
            st_map[i] = st_map.get(i) - 1
            if st_map.get(i) == 0:
                del st_map[i]
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isAnagram(s="anagram", t="nagaram"))
    print(sol.isAnagram(s="rat", t="car"))

# topic is from https://leetcode.com/problems/valid-anagram/description/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# False