# Constraints:
# m == s.length
# n == t.length
# 1 <= m, n <= 105
# s and t consist of uppercase and lowercase English letters.

class Solution:
    # solution is inspired by https://www.youtube.com/watch?v=jSto0O4AJbM&ab_channel=NeetCode
    def minWindow(self, s: str, t: str) -> str:
        hashmap_t = dict()
        hashmap_s = dict()
        for i in t:
            if i not in hashmap_t.keys():
                hashmap_t[i] = 1
                hashmap_s[i] = 0
            else:
                hashmap_t[i] += 1
        target_items = len(hashmap_t)
        have_items = 0
        minimum_sub = ''
        minimun_len = 0
        start = 0
        for stop in range(len(s)):
            if s[stop] in hashmap_t.keys():
                hashmap_s[s[stop]] += 1
                # only increase the got item numbers when they are equal, excluding the greater condition
                if hashmap_s[s[stop]] == hashmap_t[s[stop]]:
                    have_items += 1
            # simplify the compare of equal hashmap items by the total keys number
            while have_items == target_items:
                if minimun_len == 0 or minimun_len > (stop - start + 1):
                    minimun_len = stop - start + 1
                    minimum_sub = s[start:stop + 1]

                if s[start] in hashmap_t.keys():
                    hashmap_s[s[start]] -= 1
                    # due to condition "while have_items == target_items:"
                    # hashmap_s[s[start]] -= 1 only execute once,
                    # no need of "if hashmap_s[s[start]] == 0:"
                    if hashmap_s[s[start]] < hashmap_t[s[start]]:
                        have_items -= 1
                start += 1
        return minimum_sub


if __name__ == '__main__':
    sol = Solution()
    print(sol.minWindow(s="ADOBECODEBANC", t="ABC"))
    print(sol.minWindow(s="a", t="a"))
    print(sol.minWindow(s="a", t="aa"))
    print(sol.minWindow(s="aa", t="aa"))

# topic is from https://leetcode.com/problems/minimum-window-substring/submissions/1148917074/?envType=study-plan-v2&envId=top-interview-150
# output
# BANC
# a
#
# aa