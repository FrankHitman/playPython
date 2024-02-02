# Constraints:
# 1 <= s.length <= 5 * 104
# t.length == s.length
# s and t consist of any valid ascii character.


class Solution:
    # 48ms runtime
    def isIsomorphic(self, s: str, t: str) -> bool:
        s_len = len(s)
        t_len = len(t)
        if s_len != t_len:
            return False
        st_map = {}
        # s = "paper", t = "title"
        # s="badc", t="baba"
        ts_map = {}
        for i in range(s_len):
            if t[i] not in ts_map.keys():
                ts_map[t[i]] = s[i]

            if s[i] not in st_map.keys():
                st_map[s[i]] = t[i]

            if t[i] != st_map.get(s[i]) or s[i] != ts_map.get(t[i]):
                return False
        return True

    # other people's solution on leetcode with 42ms runtime
    def isIsomorphic2(self, s: str, t: str) -> bool:
        dict = {}

        for i in range(len(s)):
            if s[i] in dict:
                if dict[s[i]] != t[i]:
                    return False
            else:
                if t[i] not in dict.values():
                    dict[s[i]] = t[i]
                else:
                    return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isIsomorphic(s="egg", t="add"))
    print(sol.isIsomorphic(s="foo", t="bar"))
    print(sol.isIsomorphic(s="paper", t="title"))
    print(sol.isIsomorphic(s="badc", t="baba"))  # expected false

# topic is from https://leetcode.com/problems/isomorphic-strings/description/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# False
# True
# False
