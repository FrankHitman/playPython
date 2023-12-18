# Example 1:
# Input: nums = [1,1,1,2,2,3]
# Output: 5, nums = [1,1,2,2,3,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:
# Input: nums = [0,0,1,1,1,1,2,3,3]
# Output: 7, nums = [0,0,1,1,2,3,3,_,_]
# Explanation: Your function should return k = 7, with the first seven elements of nums being 0, 0, 1, 1, 2, 3 and 3 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Constraints:
# 1 <= nums.length <= 3 * 104
# -104 <= nums[i] <= 104
# nums is sorted in non-decreasing order.

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i = 2
        j = 2
        while j < len(nums):
            if nums[i - 2] < nums[j]:
                nums[i] = nums[j]
                i += 1
                j += 1
            else:
                j += 1

        print(i)
        print(nums)
        return i


if __name__ == '__main__':
    sol = Solution()
    sol.removeDuplicates([1, 1, 1, 2, 2, 3])
    sol.removeDuplicates([0, 0, 1, 1, 1, 1, 2, 3, 3])
    sol.removeDuplicates([1, 2, 3, 4, 5, ])

# derived from https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
# idea from https://leetcode.cn/problems/remove-duplicates-from-sorted-array-ii/solutions/702644/shan-chu-pai-xu-shu-zu-zhong-de-zhong-fu-yec2/?envType=study-plan-v2&envId=top-interview-150
# output
# 5
# [1, 1, 2, 2, 3, 3]
# 7
# [0, 0, 1, 1, 2, 3, 3, 3, 3]
# 5
# [1, 2, 3, 4, 5]
