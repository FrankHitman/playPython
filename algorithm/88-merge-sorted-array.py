class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        a = m - 1
        b = n - 1
        c = m + n - 1
        if m == 0:
            nums1 = nums2[:]
        while a >= 0 and b >= 0:
            if nums1[a] < nums2[b]:
                nums1[c] = nums2[b]
                b = b - 1
                c = c - 1
            else:
                nums1[c] = nums1[a]
                a = a - 1
                c = c - 1
        if b >= 0:
            nums1[:b + 1] = nums2[:b + 1]
        print(nums1)


if __name__ == '__main__':
    solution = Solution()
    solution.merge([0], 0, [1], 1)
    solution.merge([1], 1, [], 0)
    solution.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
    solution.merge([2, 0], 1, [1], 1)
    solution.merge([1, 2, 3, 0, 0, 0], 3, [4, 5, 6], 3)
    solution.merge([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3)

# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
# O(m+n) time
# [1]
# [1]
# [1, 2, 2, 3, 5, 6]
