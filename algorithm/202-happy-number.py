# Constraints:
# 1 <= n <= 2^31 - 1

# inspired by https://leetcode.com/problems/happy-number/description/comments/1568326
# It can be proved that if n is not a happy number,
# It will finally goto a
# 4→16→37→58→89→145→42→20→4 loop.
# so just consider if go to one of these number, it will be not happy number, otherwise, it will finally stop at 1
# The Hint is that for n > 100, the next number will less than n

class Solution:
    def __init__(self):
        self.unhappy_n = set()
        self.happy_n = set()
        self.undetermined = set()

    def isHappy(self, n: int) -> bool:
        if n in self.happy_n:
            return True
        if n in self.unhappy_n:
            return False
        if self.check_happy(n):
            self.happy_n.update(self.undetermined)
            return True
        else:
            self.unhappy_n.update(self.undetermined)
            return False

    def check_happy(self, n: int):
        self.undetermined.add(n)
        sum_squ = self.get_sum(n)
        if sum_squ == 1:
            return True
        else:
            if sum_squ in self.undetermined:
                return False
            else:
                return self.check_happy(sum_squ)

    def get_sum(self, n: int):
        sum_squ = 0
        while n > 0:
            sum_squ += (n % 10) * (n % 10)
            n = n // 10
        return sum_squ

if __name__ == '__main__':
    sol = Solution()
    print(sol.isHappy(19))
    print(sol.isHappy(2))
    print(sol.isHappy(3))
    print(sol.isHappy(4))
    print(sol.isHappy(5))
    print(sol.isHappy(6))
    print(sol.isHappy(7))
    print(sol.isHappy(8))
    print(sol.isHappy(9))
    print(sol.isHappy(10))
    print(sol.isHappy(11))

# topic is from https://leetcode.com/problems/happy-number/description/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# False
# False
# False
# False
# False
# True
# False
# True
# True
# False