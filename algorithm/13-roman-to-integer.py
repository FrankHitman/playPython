# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Example 1:
#
# Input: s = "III"
# Output: 3
# Explanation: III = 3.
# Example 2:
#
# Input: s = "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# Example 3:
#
# Input: s = "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

class Solution:
    def romanToInt(self, s: str) -> int:
        rom_map = {'I': 1,
                   'V': 5,
                   'X': 10,
                   'L': 50,
                   'C': 100,
                   'D': 500,
                   'M': 1000,
                   }
        index = 0
        result = 0
        while index < len(s):
            if index < len(s) - 1:
                if rom_map[s[index]] >= rom_map[s[index + 1]]:
                    result += rom_map[s[index]]
                    index += 1
                else:
                    result += rom_map[s[index + 1]] - rom_map[s[index]]
                    index += 2
            else:
                result += rom_map[s[index]]
                index += 1
        print(s, result)
        return result

    # copy from other people's leetcode submission with 42ms runtime
    def romanToInt2(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        for i in range(len(s) - 1):
            if romans[s[i]] < romans[s[i + 1]]:
                result -= romans[s[i]]
            else:
                result += romans[s[i]]
        result += romans[s[-1]]
        return result

    # copy from other people's leetcode submission with 42ms runtime
    def romanToInt3(self, s: str) -> int:
        translations = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        number = 0
        s = s.replace("IV", "IIII").replace("IX", "VIIII")
        s = s.replace("XL", "XXXX").replace("XC", "LXXXX")
        s = s.replace("CD", "CCCC").replace("CM", "DCCCC")
        for char in s:
            number += translations[char]
        return number


if __name__ == '__main__':
    sol = Solution()
    sol.romanToInt("III")
    sol.romanToInt("LVIII")
    sol.romanToInt("MCMXCIV")

# topic is from https://leetcode.com/problems/roman-to-integer/submissions/1133556389/?envType=study-plan-v2&envId=top-interview-150
# runtime 72ms
# output
# III 3
# LVIII 58
# MCMXCIV 1994