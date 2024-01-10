# 1 <= s.length <= 2 * 105
# s consists only of printable ASCII characters.
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pattern = re.compile('\W')
        pattern = re.compile('[^a-zA-Z0-9]*')
        s = re.sub(pattern, '', s)
        s = s.lower()
        print(s)
        i = 0
        j = len(s) - 1
        while i < j:
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    # other people's solution on leetcode
    def isPalindrome2(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left <= right:
            if s[left].isalnum() == False:
                left += 1
                continue
            if s[right].isalnum() == False:
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.isPalindrome(s="A man, a plan, a canal: Panama"))
    print(sol.isPalindrome(s="race a car"))
    print(sol.isPalindrome(s=" "))
    print(sol.isPalindrome(s="ab_a"))
