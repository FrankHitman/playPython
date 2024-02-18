# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.
#
# Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

class Solution:
    # inspired by collection.defaultdict
    # 65ms runtime
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        indices_map = {}
        for k, v in enumerate(nums):
            indices_map.setdefault(v, []).append(k)

        # return a new list https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list
        # sorted(nums)
        i = 0
        j = len(nums) - 1
        nums.sort()
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [indices_map[nums[i]].pop(), indices_map[nums[j]].pop()]
        return []


    # brute force way solution with 946ms runtime
    def twoSum1(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            second = target - nums[i]
            for j in range(i + 1, len(nums), 1):
                if nums[j] == second:
                    return [i, j]
        return []

    # not valid, such as [3,3] return [1,1]
    def twoSum2(self, nums: list[int], target: int) -> list[int]:
        i = 0
        j = len(nums) - 1
        indices_map = {}
        for k, v in enumerate(nums):
            indices_map[v] = k

        # return a new list https://docs.python.org/3/faq/design.html#why-doesn-t-list-sort-return-the-sorted-list
        # sorted(nums)
        nums.sort()
        while i < j:
            if nums[i] + nums[j] > target:
                j -= 1
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                return [indices_map[nums[i]], indices_map[nums[j]]]
        return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.twoSum(nums=[2, 7, 11, 15], target=9))
    print(sol.twoSum(nums=[3, 2, 4], target=6))
    print(sol.twoSum(nums=[3, 3], target=6))

# topic is from https://leetcode.com/problems/two-sum/description/?envType=study-plan-v2&envId=top-interview-150
# output
#
