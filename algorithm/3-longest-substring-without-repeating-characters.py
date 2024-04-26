# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of English letters, digits, symbols and spaces.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        s_set = set()
        longest_len = 0
        # sliding window algorithm, start and stop are two pointers.
        start = 0
        for stop in range(len(s)):
            if s[stop] not in s_set:
                s_set.add(s[stop])
                if longest_len == 0 or len(s_set) > longest_len:
                    longest_len = len(s_set)
            else:
                s_set.add(s[stop])
                # it's required to move start pointer to next position of the duplicate character position
                while start < stop:
                    if s[start] == s[stop]:
                        start += 1
                        break
                    s_set.remove(s[start])
                    start += 1
        return longest_len


if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLongestSubstring(s="abcabcbb"))
    print(sol.lengthOfLongestSubstring(s="bbbbb"))
    print(sol.lengthOfLongestSubstring(s="pwwkew"))
    print(sol.lengthOfLongestSubstring(s="qrsvbspk"))
# qrsvbspk once encounter 's'=='s', it's required to move start pointer to the duplicate 's' position
# meaning cannot include both s, such as svbs

# topic is from https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1147863290/?envType=study-plan-v2&envId=top-interview-150
# output
# 3
# 1
# 3
# 5