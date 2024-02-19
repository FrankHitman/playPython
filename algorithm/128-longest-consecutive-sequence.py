# Constraints:
# 0 <= nums.length <= 105
# -109 <= nums[i] <= 109

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
class Solution:
    # other people's solution on leetcode with 313ms runtime
    def longestConsecutive(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        longest = 1

        nums_set = set(nums)
        for i in nums_set:
            if (i - 1) in nums_set:
                continue
            else:
                start = i
                while (i + 1) in nums_set:
                    i += 1
                longest = (i - start + 1) if (i - start + 1) > longest else longest
        return longest

    # inspired by https://leetcode.com/problems/longest-consecutive-sequence/description/comments/1574147
    # 5825ms runtime, idea saved as 128-consecutive-consequence.png
    def longestConsecutive1(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0
        longest = 1

        nums_set = set()
        for i in nums:
            nums_set.add(i)
        for i in nums:
            if (i - 1) in nums_set:
                continue
            else:
                count = 1
                while (i + 1) in nums_set:
                    count += 1
                    i += 1
                longest = count if count > longest else longest
        return longest

    # not valid for test case [1, 2, 0, 1]
    def longestConsecutive2(self, nums: list[int]) -> int:
        if len(nums) == 1:
            return 1
        if len(nums) == 0:
            return 0

        nums.sort()
        start, longest = 0, 1
        # using sliding window algorithm
        for stop in range(1, len(nums)):
            if nums[stop] - nums[start] == stop - start:
                longest = (stop - start + 1) if (stop - start + 1) > longest else longest
            else:
                start = stop
        return longest


if __name__ == '__main__':
    sol = Solution()
    print(sol.longestConsecutive(nums=[100, 4, 200, 1, 3, 2]))
    print(sol.longestConsecutive(nums=[0, 3, 7, 2, 5, 8, 4, 6, 0, 1]))
    print(sol.longestConsecutive(nums=[0, 1, 2, 4, 5, 6, 7, 8]))
    print(sol.longestConsecutive(nums=[0, 1, 2, 3, 4, 6, 7]))
    print(sol.longestConsecutive([0]))
    print(sol.longestConsecutive([0, 0]))
    print(sol.longestConsecutive([1, 2, 0, 1]))  # expected 3

# topic is from https://leetcode.com/problems/longest-consecutive-sequence/description/?envType=study-plan-v2&envId=top-interview-150
# output
# 4
# 9
# 5
# 5
# 1
# 1
# 3
