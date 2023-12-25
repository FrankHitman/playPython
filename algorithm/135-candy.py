# idea is from https://www.youtube.com/watch?v=1IzCRCcK17A&ab_channel=NeetCodeIO

class Solution:
    def candy(self, ratings: list[int]) -> int:
        total_candy = 0
        index = 1
        candy_list = [1 for _ in range(len(ratings))]
        while 0 < index < len(ratings):
            if ratings[index - 1] < ratings[index]:
                candy_list[index] = candy_list[index - 1] + 1
            index += 1
        while index > 1:
            index -= 1
            if ratings[index - 1] > ratings[index]:
                if candy_list[index - 1] > candy_list[index]:
                    continue
                else:
                    candy_list[index - 1] = candy_list[index] + 1

        for candy in candy_list:
            total_candy += candy
        print(candy_list)
        return total_candy


if __name__ == '__main__':
    sol = Solution()
    print(sol.candy([1, 0, 2]))
    print(sol.candy([1, 2, 2]))
    print(sol.candy([2, 100, 100, 100]))
    print(sol.candy([1, 2, 3, 4, 5]))
    print(sol.candy([5, 4, 3, 2, 1]))
    print(sol.candy([1, 2, 100, 50, 4, 10]))
    print(sol.candy([5, 4, 3, 5, 6, 2]))

# topic is from https://leetcode.com/problems/candy/?envType=study-plan-v2&envId=top-interview-150
# output
# [2, 1, 2]
# 5
# [1, 2, 1]
# 4
# [1, 2, 1, 1]
# 5
# [1, 2, 3, 4, 5]
# 15
# [5, 4, 3, 2, 1]
# 15
# [1, 2, 3, 2, 1, 2]
# 11
# [3, 2, 1, 2, 3, 1]
# 12
