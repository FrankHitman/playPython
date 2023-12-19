# Example 1:
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
# Constraints:
# 1 <= nums.length <= 105
# -231 <= nums[i] <= 231 - 1
# 0 <= k <= 105

class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k > len(nums):
            k = k % len(nums)
        nums.reverse()
        a = nums[:k]
        a.reverse()
        b = nums[k:]
        b.reverse()
        nums[:k] = a
        nums[k:] = b
        print(nums)

    def rotate2(self, nums2: list[int], k: int) -> None:
        if k > len(nums2):
            k = k % len(nums2)
        aa = nums2[::-1]
        bb = aa[:k]
        cc = aa[k:]
        nums2[:k] = bb[::-1]
        nums2[k:] = cc[::-1]
        print(nums2)


if __name__ == '__main__':
    sol = Solution()
    sol.rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3)
    sol.rotate(nums=[-1, -100, 3, 99], k=2)
    sol.rotate2(nums2=[1, 2, 3, 4, 5, 6, 7], k=3)
    sol.rotate2(nums2=[-1, -100, 3, 99], k=2)

# question from https://leetcode.com/problems/rotate-array/?envType=study-plan-v2&envId=top-interview-150
# idea from hint3
# output
# [5, 6, 7, 1, 2, 3, 4]
# [3, 99, -1, -100]
# [5, 6, 7, 1, 2, 3, 4]
# [3, 99, -1, -100]