# Constraints:
# 1 <= ransomNote.length, magazine.length <= 105
# ransomNote and magazine consist of lowercase English letters.


class Solution:
    # 80ms runtime
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        mag_map = {}
        ran_map = {}
        mag_len = len(magazine)
        ran_len = len(ransomNote)
        max_len = mag_len if mag_len > ran_len else ran_len
        i = 0
        while i < max_len:
            if i < mag_len:
                mag_map[magazine[i]] = mag_map.get(magazine[i], 0) + 1
            if i < ran_len:
                ran_map[ransomNote[i]] = ran_map.get(ransomNote[i], 0) + 1
            i += 1

        for i in ran_map.keys():
            if ran_map.get(i) > mag_map.get(i, 0):
                return False
        return True

    # other people's solution from leetcode website with 61ms runtime
    def canConstruct2(self, ransomNote: str, magazine: str) -> bool:
        m = {}
        for c in magazine:
            m[c] = m.get(c, 0) + 1

        for c in ransomNote:
            if c not in m:
                return False
            m[c] -= 1
            if m[c] == 0:
                del m[c]
        return True


if __name__ == '__main__':
    sol = Solution()
    print(sol.canConstruct(ransomNote="a", magazine="b"))
    print(sol.canConstruct(ransomNote="aa", magazine="ab"))
    print(sol.canConstruct(ransomNote="aa", magazine="aab"))

# topic is from https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150
# output
# False
# False
# True
