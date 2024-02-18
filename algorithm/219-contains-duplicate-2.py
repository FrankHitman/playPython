# Constraints:
# 1 <= nums.length <= 105
# -109 <= nums[i] <= 109
# 0 <= k <= 105

from collections import defaultdict


class Solution:
    # other people's solution on leetcode with 448ms runtime
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        vk_map = {}
        for key, v in enumerate(nums):
            if v in vk_map:
                if key - vk_map[v] <= k:
                    return True
            vk_map[v] = key
        return False

    # my solution with 522ms runtime
    def containsNearbyDuplicate1(self, nums: list[int], k: int) -> bool:
        vk_map = defaultdict(list)
        for key, v in enumerate(nums):
            vk_map[v].append(key)
        for indices in vk_map.values():
            if len(indices) > 1:
                indices.sort()
                i = 0
                j = 1
                while i < j < len(indices):
                    if indices[j] - indices[i] <= k:
                        return True
                    else:
                        i += 1
                        j += 1
        return False


if __name__ == '__main__':
    sol = Solution()
    print(sol.containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
    print(sol.containsNearbyDuplicate(nums=[1, 0, 1, 1], k=1))
    print(sol.containsNearbyDuplicate(nums=[1, 2, 3, 1, 2, 3], k=2))

# topic is from https://leetcode.com/problems/contains-duplicate-ii/description/?envType=study-plan-v2&envId=top-interview-150
# output
# True
# True
# False