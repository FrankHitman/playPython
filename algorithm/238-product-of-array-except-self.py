# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
#
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
#
# You must write an algorithm that runs in O(n) time and without using the division operation.
#
# Example 1:
# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:
# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
#
# Constraints:
# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        product = 1
        zero_count = 0
        zero_index = -1
        for i, v in enumerate(nums):
            if v == 0:
                zero_index = i
                zero_count += 1
                continue
            product = product * v
        print(nums)
        if zero_count == 0:
            return [product // item for item in nums]
        elif zero_count == 1:
            product_list = [0 for _ in nums]
            product_list[zero_index] = product
            return product_list
        else:
            return [0 for _ in nums]


if __name__ == '__main__':
    sol = Solution()
    print(sol.productExceptSelf([1, 2, 3, 4]))
    print(sol.productExceptSelf([-1, 1, 0, -3, 3]))
    print(sol.productExceptSelf([-1, 1, 0, 0, 3]))

# topic is from https://leetcode.com/problems/product-of-array-except-self/submissions/1126439414/?envType=study-plan-v2&envId=top-interview-150
# output
# [1, 2, 3, 4]
# [24, 12, 8, 6]
# [-1, 1, 0, -3, 3]
# [0, 0, 9, 0, 0]
# [-1, 1, 0, 0, 3]
# [0, 0, 0, 0, 0]