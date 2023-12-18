# Example 1:
# Input: nums = [3,2,3]
# Output: 3
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        item_map = {}
        max_item = None
        for i in nums:
            if i in item_map:
                item_map[i] += 1
            else:
                item_map[i] = 1
            if max_item is None:
                max_item = i
            else:
                if item_map[max_item] < item_map[i]:
                    max_item = i
        print(max_item)
        return max_item


if __name__ == '__main__':
    sol = Solution()
    sol.majorityElement([3, 2, 3])
    sol.majorityElement([2, 2, 1, 1, 1, 2, 2])

# item from https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150
# idea from https://leetcode.cn/problems/majority-element/solutions/146074/duo-shu-yuan-su-by-leetcode-solution/?envType=study-plan-v2&envId=top-interview-150
# output
# 3
# 2