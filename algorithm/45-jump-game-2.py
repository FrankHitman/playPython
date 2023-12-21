# You are given a 0-indexed array of integers nums of length n. You are initially positioned at nums[0].
#
# Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at nums[i], you can jump to any nums[i + j] where:
#
# 0 <= j <= nums[i] and
# i + j < n
# Return the minimum number of jumps to reach nums[n - 1]. The test cases are generated such that you can reach nums[n - 1].
#
#
#
# Example 1:
#
# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
# Example 2:
#
# Input: nums = [2,3,0,1,4]
# Output: 2
#
#
# Constraints:
#
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 1000
# It's guaranteed that you can reach nums[n - 1].
class Solution:
    def jump(self, nums: list[int]) -> int:
        nums_len = len(nums)
        jump_times = 0
        if nums_len == 1:
            return jump_times
        else:
            jump_times += 1

        def getMax(nums, start, stop, jump_times):
            if stop >= (nums_len - 1):
                return jump_times
            max_value = nums[start]
            max_index = start
            while start <= stop:
                if (max_index + max_value) < (nums[start] + start):
                    max_index = start
                    max_value = nums[start]
                start += 1
            jump_times += 1
            if max_value + max_index >= nums_len - 1:
                return jump_times
            elif max_index + max_value > stop:
                return getMax(nums, max_index + 1, max_index + max_value, jump_times)
            else:
                return jump_times

        return getMax(nums, 1, nums[0], jump_times)


if __name__ == '__main__':
    sol = Solution()
    print(sol.jump([2, 3, 1, 1, 4]))
    print(sol.jump([2, 3, 0, 1, 4]))
    print(sol.jump([2, 0, 0]))
    print(sol.jump([5, 9, 3, 2, 1, 0, 2, 3, 3, 1, 0, 0]))

# topic is from https://leetcode.com/problems/jump-game-ii/submissions/1125085730/?envType=study-plan-v2&envId=top-interview-150
# The key is to finding the maximum steps in each slice. If the maximum steps is greater than the array's length, it can reach the end of the array.
# For example
# [5,9,3,2,1,0,2,3,3,1,0,0]
# The nums length is 12. The first item is 5, then get the maximum steps in the next slice nums[1:5+1]
#
# [5,9,3,2,1,0,2,3,3,1,0,0]
#  0,1,2,3,4,5,6,7,8,9,10,11
#   10,5,5,5,5
# the maximus step is 10 at index 1, then get the next maximum steps in the next slice nums[2: 10+1]
#
# [5,9,3,2,1,0,2, 3, 3, 1, 0, 0]
#  0,1,2,3,4,5,6, 7, 8, 9, 10,11
#      5,5,5,5,8,10,11,10, 10
# the maximus step is 11 at index 8, which can reach the end of array, because 11 == nums_length-1

# output
# 2
# 2
# 1
# 3