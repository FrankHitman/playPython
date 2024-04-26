class Solution:
    # my solution which cost 744ms runtime
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        output = []
        nums.sort()
        # previous is charge of remove duplicate value, guaranteeing distinct triplets.
        previous_f = None
        previous_s = None
        for first in range(len(nums) - 2):
            # add this short circuit runtime was reduced to 600ms
            if nums[first] > 0:
                return output
            if nums[first] == previous_f:
                continue
            second = first + 1
            third = len(nums) - 1
            while second < third:
                if nums[second] + nums[third] > -nums[first]:
                    third -= 1
                elif nums[second] + nums[third] < -nums[first]:
                    second += 1
                else:
                    # must exclude previous_f for instance [3,0,-2,-1,1,2] which [[-2,-1,3],[-2,0,2],[-1,0,1]] is expected
                    if nums[first] == previous_f and nums[second] == previous_s:
                        second += 1
                        continue
                    output.append([nums[first], nums[second], nums[third]])
                    previous_f = nums[first]
                    previous_s = nums[second]
                    second += 1
                    third -= 1
        return output

    # other people's solution from leetcode which cost 509ms runtime
    def threeSum2(self, nums: list[int]) -> list[list[int]]:
        triplets = []
        # sort list makes the finding more efficient
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                # if the minimum item is greater than 0, return empty.
                return triplets
            if i == 0 or nums[i] != nums[i - 1]:
                # the -nums[i] is the remaining two items' target
                self.two_sum(nums, -nums[i], i, triplets)
        return triplets

    def two_sum(self, nums, target, i, triplets):
        # two pointers
        left = i + 1
        right = len(nums) - 1
        while left < right:
            current = nums[left] + nums[right]
            if current == target:
                triplets.append([nums[i], nums[left], nums[right]])
                left += 1
                #  the solution set must not contain duplicate triplets.
                while left < right and nums[left] == nums[left - 1]:
                    left += 1
                right -= 1
            elif current < target:
                left += 1
            else:
                right -= 1


if __name__ == '__main__':
    sol = Solution()
    print(sol.threeSum(nums=[-1, 0, 1, 2, -1, -4]))
    print(sol.threeSum(nums=[0, 1, 1]))
    print(sol.threeSum(nums=[0, 0, 0]))
    print(sol.threeSum(nums=[0, 0, 0, 0]))
    print(sol.threeSum(nums=[-2, 0, 0, 2, 2]))
    print(sol.threeSum(nums=[3, 0, -2, -1, 1, 2]))

# topic is from https://leetcode.com/problems/3sum/?envType=study-plan-v2&envId=top-interview-150
# output
# [[-1, -1, 2], [-1, 0, 1]]
# []
# [[0, 0, 0]]
# [[0, 0, 0]]
# [[-2, 0, 2]]
# [[-2, -1, 3], [-2, 0, 2], [-1, 0, 1]]
