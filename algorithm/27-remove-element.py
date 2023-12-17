class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            if nums[j] == val:
                j = j - 1
                continue
            if nums[i] == val:
                nums[i] = nums[j]
                nums[j] = val
            i = i + 1
        print(i)
        print(nums)
        return i


if __name__ == '__main__':
    solution = Solution()
    solution.removeElement([0, 1, 2, 2, 3, 0, 4, 2], 2)
    solution.removeElement([3, 2, 2, 3], 3)
    solution.removeElement([3], 3)

# output https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150
# 5
# [0, 1, 4, 0, 3, 2, 2, 2]
# 2
# [2, 2, 3, 3]
# 0
# [3]
