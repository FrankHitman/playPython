# Constraints:
# n == height.length
# 2 <= n <= 105
# 0 <= height[i] <= 104

# hint2: Try to use two-pointers. Set one pointer to the left and one to the right of the array.
# Always move the pointer that points to the lower line.

class Solution:
    def maxArea(self, height: list[int]) -> int:
        # the maximum on x-axis direction
        product = min(height[0], height[-1]) * (len(height) - 1)
        i = 0
        j = len(height) - 1
        while i < j:
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
            if min(height[i], height[j]) * (j - i) > product:
                product = min(height[i], height[j]) * (j - i)
        return product


if __name__ == '__main__':
    sol = Solution()
    print(sol.maxArea(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]))
    print(sol.maxArea(height=[1, 1]))

# topic is from https://leetcode.com/problems/container-with-most-water/submissions/1146060004/?envType=study-plan-v2&envId=top-interview-150
# output
# 49
# 1
