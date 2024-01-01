# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# Constraints:
# 1 <= num <= 3999

class Solution:
    def intToRoman(self, num: int) -> str:
        rom_map = {1: "I",
                   5: "V",
                   10: "X",
                   50: "L",
                   100: "C",
                   500: "D",
                   1000: "M", }
        int_list = [1000, 500, 100, 50, 10, 5, 1]
        rom_str = ''
        for i in int_list:
            rom_nums = num // i
            num = num % i
            rom_str += rom_map[i] * rom_nums
        print(rom_str)
        rom_str = rom_str.replace("VIIII", "IX").replace("IIII", "IV")
        rom_str = rom_str.replace("LXXXX", "XC").replace("XXXX", "XL")
        rom_str = rom_str.replace("DCCCC", "CM").replace("CCCC", "CD")
        print(rom_str)
        return rom_str

    # other people's leetcode code with 42ms runtime
    def intToRoman2(self, num: int) -> str:
        mapping = {
            1: "I",
            4: "IV",
            5: "V",
            9: "IX",
            10: "X",
            40: "XL",
            50: "L",
            90: "XC",
            100: "C",
            400: "CD",
            500: "D",
            900: "CM",
            1000: "M",
        }

        ans = ""
        values = reversed(mapping.keys())
        for val in values:
            while num >= val:
                ans += mapping[val]
                num -= val
        return ans


if __name__ == '__main__':
    sol = Solution()
    sol.intToRoman(3999)
    sol.intToRoman(4)
    sol.intToRoman(58)
    sol.intToRoman(1994)

# topic is from https://leetcode.com/problems/integer-to-roman/submissions/1133588868/?envType=study-plan-v2&envId=top-interview-150
# output 79ms runtime
# MMMDCCCCLXXXXVIIII
# MMMCMXCIX
# IIII
# IV
# LVIII
# LVIII
# MDCCCCLXXXXIIII
# MCMXCIV
