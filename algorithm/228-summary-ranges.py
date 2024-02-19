# Constraints:
# 0 <= nums.length <= 20
# -231 <= nums[i] <= 231 - 1
# All the values of nums are unique.
# nums is sorted in ascending order.


class Solution:
    # using sliding window algorithm
    def summaryRanges(self, nums: list[int]) -> list[str]:
        if len(nums) == 1:
            return ['{}'.format(nums[0])]
        start = 0
        result = []
        for stop in range(1, len(nums)):
            if (stop - start) != (nums[stop] - nums[start]):
                if nums[start] == nums[stop - 1]:
                    result.append('{}'.format(nums[start]))
                else:
                    result.append('{}->{}'.format(nums[start], nums[stop - 1]))
                start = stop
            if stop == len(nums) - 1:
                if nums[start] == nums[stop]:
                    result.append('{}'.format(nums[start]))
                else:
                    result.append('{}->{}'.format(nums[start], nums[stop]))
        return result


if __name__ == '__main__':
    sol = Solution()
    print(sol.summaryRanges(nums=[0, 1, 2, 4, 5, 7]))
    print(sol.summaryRanges(nums=[0, 2, 3, 4, 6, 8, 9]))
    print(sol.summaryRanges([-1]))

# topic is from https://leetcode.com/problems/summary-ranges/description/?envType=study-plan-v2&envId=top-interview-150
# output
# ['0->2', '4->5', '7']
# ['0', '2->4', '6', '8->9']
# ['-1']