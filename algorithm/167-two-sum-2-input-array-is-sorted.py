# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] < target:
                i += 1
            elif numbers[i] + numbers[j] > target:
                j -= 1
            else:
                return [i + 1, j + 1]
        return None


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(numbers=[2, 7, 11, 15], target=9))
    print(sol.twoSum(numbers=[2, 3, 4], target=6))
    print(sol.twoSum(numbers=[-1, 0], target=-1))

# topic is from https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/submissions/1145854561/?envType=study-plan-v2&envId=top-interview-150
# output
# [1, 2]
# [1, 3]
# [1, 2]