class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # idea from https://www.youtube.com/watch?v=0iDiUuHZE_g&ab_channel=AlgoEngine
        # find the longest proper prefix that is also a suffix
        # we pre-process pattern and prepare an integer array lps[] that tells us the count of characters to be skipped
        lps = [0] * len(needle)
        pre = 0
        for i in range(1, len(needle)):
            while (pre > 0 and needle[i] != needle[pre]):
                pre = lps[pre - 1]
            if needle[i] == needle[pre]:
                pre += 1
                lps[i] = pre

        n = 0  # needle index
        for h in range(len(haystack)):
            while (n > 0 and needle[n] != haystack[h]):
                n = lps[n - 1]
            if needle[n] == haystack[h]:
                n += 1
            if n == len(needle):
                return h - n + 1
        return -1

        # return haystack.find(needle)


if __name__ == '__main__':
    sol = Solution()
    print(sol.strStr(haystack="sadbutsad", needle="sad"))
    print(sol.strStr(haystack="leetcode", needle="leeto"))

#  A  A  B  A  A  C  A  A  B  A  A
# [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
# For the pattern “AAAA”, lps[] is [0, 1, 2, 3]
# For the pattern “ABCDE”, lps[] is [0, 0, 0, 0, 0]
# For the pattern “AABAACAABAA”, lps[] is [0, 1, 0, 1, 2, 0, 1, 2, 3, 4, 5]
# For the pattern “AAACAAAAAC”, lps[] is [0, 1, 2, 0, 1, 2, 3, 3, 3, 4]
# For the pattern “AAABAAA”, lps[] is [0, 1, 2, 0, 1, 2, 3]
# KMP algorithm explanation from https://www.geeksforgeeks.org/kmp-algorithm-for-pattern-searching/
