# inspired by https://leetcode.com/problems/trapping-rain-water/description/comments/2162730
class Solution:
    def trap(self, height: list[int]) -> int:
        total_trapped = 0
        index_left = 0
        length = len(height)
        higher_left = height[0]
        higher_list_left = [0 for _ in range(length)]
        higher_list_right = [0 for _ in range(length)]
        higher_right = height[length - 1]
        index_right = length - 1
        index_right -= 1
        higher_list_left[0] = higher_left
        higher_list_right[length - 1] = higher_right

        while 0 <= index_left < length - 1 \
                and 0 <= index_right < length - 1:
            higher_left = max(higher_left, height[index_left + 1])
            higher_list_left[index_left + 1] = higher_left

            higher_right = max(height[index_right], higher_right)
            higher_list_right[index_right] = higher_right

            index_left += 1
            index_right -= 1
        print(higher_list_left)
        print(higher_list_right)
        for i in range(length):
            total_trapped += min(higher_list_left[i], higher_list_right[i]) - height[i]
        return total_trapped


if __name__ == '__main__':
    sol = Solution()
    print(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
    print(sol.trap([4, 2, 0, 3, 2, 5]))

# topic is from https://leetcode.com/problems/trapping-rain-water/?envType=study-plan-v2&envId=top-interview-150
# output
# [0, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 3]
# [3, 3, 3, 3, 3, 3, 3, 3, 2, 2, 2, 1]
# 6
# [4, 4, 4, 4, 4, 5]
# [5, 5, 5, 5, 5, 5]
# 9