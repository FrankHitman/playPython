# Constraints:
# 1 <= target <= 109
# 1 <= nums.length <= 105
# 1 <= nums[i] <= 104
# You are asked to find a subarray (contiguous elements), not a subsequence.
# idea is inspired by https://janac.medium.com/what-is-the-sliding-window-algorithm-f9fcfe92b853
# sliding window algorithm
class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sum_val = 0
        min_sub_len = 0
        start = 0
        for stop in range(len(nums)):
            sum_val += nums[stop]
            while sum_val >= target:
                if min_sub_len == 0 or min_sub_len > (stop - start + 1):
                    min_sub_len = stop - start + 1

                sum_val -= nums[start]
                start += 1
        return min_sub_len
        # nums.sort()
        # sum = 0
        # items = []
        # for i in range(len(nums) - 1, -1, -1):
        #     if nums[i] + sum >= target:
        #         return len(items) + 1
        #     else:
        #         items.append(nums[i])
        #         sum += nums[i]
        # return 0


if __name__ == '__main__':
    sol = Solution()
    print(sol.minSubArrayLen(target=7, nums=[2, 3, 1, 2, 4, 3]))
    print(sol.minSubArrayLen(target=4, nums=[1, 4, 4]))
    print(sol.minSubArrayLen(target=11, nums=[1, 1, 1, 1, 1, 1, 1, 1]))
    print(sol.minSubArrayLen(target=213, nums=[12, 28, 83, 4, 25, 26, 25, 2, 25, 25, 25, 12]))

# topic is from https://leetcode.com/problems/minimum-size-subarray-sum/description/?envType=study-plan-v2&envId=top-interview-150
# output
# 2
# 1
# 0
# 8