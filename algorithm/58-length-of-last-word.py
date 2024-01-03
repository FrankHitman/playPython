class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s_list = s.split()
        print(s_list)
        return len(s_list[-1])

if __name__ == '__main__':
    sol = Solution()
    print(sol.lengthOfLastWord("Hello World"))
    print(sol.lengthOfLastWord("   fly me   to   the moon  "))
    print(sol.lengthOfLastWord("luffy is still joyboy"))

# topic is from https://leetcode.com/problems/length-of-last-word/submissions/1135647982/?envType=study-plan-v2&envId=top-interview-150
# output
# ['Hello', 'World']
# 5
# ['fly', 'me', 'to', 'the', 'moon']
# 4
# ['luffy', 'is', 'still', 'joyboy']
# 6