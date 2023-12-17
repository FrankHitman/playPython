class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 0
        j = 1
        while i < j < len(nums):
            if nums[i] < nums[j]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        i += 1
        print(i)
        print(nums)
        return i


if __name__ == '__main__':
    sol = Solution()
    sol.removeDuplicates([1, 1, 2], )
    sol.removeDuplicates([0, 0, 1, 1, 1, 2, 2, 3, 3, 4])

# output https://leetcode.com/problems/remove-duplicates-from-sorted-array/?envType=study-plan-v2&envId=top-interview-150
# 2
# [1, 2, 2]
# 5
# [0, 1, 2, 3, 4, 2, 2, 3, 3, 4]
