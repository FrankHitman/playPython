class Solution:
    def reverseWords(self, s: str) -> str:
        s_l = s.split()
        reverse_s = ""
        for index in range(len(s_l) - 1, -1, -1):
            if index == len(s_l) - 1:
                reverse_s += s_l[index]
            else:
                reverse_s += " " + s_l[index]
        return reverse_s

    # other people's solution from leetcode
    def reverseWords2(self, s: str) -> str:
        return ' '.join(reversed(s.split()))


if __name__ == '__main__':
    sol = Solution()
    print(sol.reverseWords("the sky is blue"))
    print(sol.reverseWords("  hello world  "))
    print(sol.reverseWords("a good   example"))

# topic is from https://leetcode.com/problems/reverse-words-in-a-string/submissions/1138410018/?envType=study-plan-v2&envId=top-interview-150
# output
# blue is sky the
# world hello
# example good a